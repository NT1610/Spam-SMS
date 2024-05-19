from playwright.async_api import async_playwright
from playwright_stealth import stealth_async
from bs4 import BeautifulSoup
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from underthesea import word_tokenize
import time
import re
import asyncio
import psycopg2
from crawl.acc_pass import (
    ACCOUNT,
    PASS,
    USER_DATA_DIR,
    HOST_DB,
    NAME_DB,
    USER_DB,
    PASSWORD_DB,
)


class FacebookScraper:
    CHROMIUM_ARGS = ["--disable-blink-features=AutomationControlled"]

    def __init__(self, login_url, post_url):
        self.login_url = login_url
        self.post_url = post_url
        self.browser = None
        self.page = None
        self.soup = None

    async def sign_out(self):
        await self.page.locator(
            "//div[@class='x1rg5ohu x1n2onr6 x3ajldb x1ja2u2z']"
        ).first.click()
        await self.page.wait_for_timeout(500)
        await self.page.locator("//div[@role='listitem'][5]").click()

    async def load_more_comments(self):
        start_time = time.time()
        try:
            while (
                await self.page.get_by_role("button", name="Xem thêm bình luận")
                is not None
            ):
                await self.page.get_by_role("button", name="Xem thêm bình luận").click(
                    timeout=2000
                )
                print("Loading more comments...")
                await self.page.wait_for_timeout(1000)
        except Exception as e:
            print("Error loading more comments:", e)
        end_time = time.time()
        print("Loaded all comments in", str(end_time - start_time), "seconds")

    async def block_resources(self, route):
        if route.request.resource_type in ["image", "media"]:
            await route.abort()
        elif ".mp4" in route.request.url:
            await route.abort()
        else:
            await route.continue_()

    async def show_all_comments(self):
        await self.page.get_by_label("Viết bình luận", exact=True).click()
        await self.page.locator(
            "//div[@class='x6s0dn4 x78zum5 xdj266r x11i5rnm xat24cr x1mh8g0r xe0p6wg']"
        ).click()
        await self.page.wait_for_timeout(1000)
        await self.page.get_by_role("menuitem").last.click()
        await self.page.wait_for_timeout(1000) #3000

    async def click_read_more(self):
        try:
            while True:
                await self.page.get_by_role("button", name="Xem thêm").first.click()
                await self.page.wait_for_timeout(500)
        except Exception as e:
            print("Finished expanding comments:", e)

    @staticmethod
    def remove_stopword(input_text):
        with open(r"G:\Year3\DataMining\CuoiKi\Spam-SMS\backend\Code\crawl\vietnamese-stopwords.txt", "r", encoding="utf8") as f:
            stop_words = f.readlines()
            stop_words = set(m.strip() for m in stop_words)
        words = word_tokenize(input_text)
        filtered_words = [word for word in words if word.lower() not in stop_words]
        return " ".join(filtered_words)

    def extract_comment(self):
        output = []
        text = ""
        pattern = r"/user/(\d+)/"
        comments = self.soup.find_all("div", class_="x1y1aw1k xn6708d xwib8y2 x1ye3gou")
        for comment in comments:
            user_link = comment.find("a").get("href")
            match = re.search(pattern, user_link)
            if match:
                user_id = match.group(1)
            else:
                user_id = None
            user = comment.find("span", class_="x3nfvp2").get_text()
            try:
                cmt = comment.find("div", {"dir": "auto"}).get_text()
            except:
                cmt = "#sticker"

            text = " ".join([text, cmt])
            output.append([user_id, user, cmt])
        text = self.remove_stopword(text)
        return output, text

    @staticmethod
    def visualize_text(text):
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(
            text
        )
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()

    @staticmethod
    def store_to_db(data):
        try:
            db_conn = psycopg2.connect(
                host=HOST_DB, database=NAME_DB, user=USER_DB, password=PASSWORD_DB
            )
            cursor = db_conn.cursor()

            create_table_query = """
                CREATE TABLE IF NOT EXISTS facebook_comments (
                    user_id VARCHAR(255),
                    user_name VARCHAR(255),
                    comment_text TEXT
                );
            """
            cursor.execute(create_table_query)

            for record in data:
                insert_query = """
                    INSERT INTO facebook_comments (user_id, user_name, comment_text)
                    VALUES (%s, %s, %s);
                """
                cursor.execute(insert_query, (record[0], record[1], record[2]))

            db_conn.commit()
            cursor.close()
            db_conn.close()
        except Exception as e:
            print("Error storing data to database:", e)

    async def scrape(self):
        async with async_playwright() as p:
            self.browser = await p.chromium.launch_persistent_context(
                user_data_dir=USER_DATA_DIR,
                channel="chrome",
                headless=False,
                slow_mo=20,
                args=self.CHROMIUM_ARGS,
                ignore_default_args=["--enable-automation"],
            )
            self.page = await self.browser.new_page()
            await stealth_async(self.page)
            await self.page.route("**/*", self.block_resources)
            await self.page.goto(self.login_url, timeout=0)
            await self.page.goto(self.post_url)
            await self.page.wait_for_timeout(2000)

            try:
                await self.show_all_comments()
                await self.load_more_comments()
                await self.click_read_more()
            except Exception as e:
                print("Error during scraping:", e)
                await self.sign_out()
            finally:
                await self.page.wait_for_load_state("networkidle")
                self.soup = BeautifulSoup(await self.page.content(), "lxml")
                await self.page.wait_for_timeout(1000)
                await self.page.close()
                await self.browser.close()

    def save_data(self, output):
        columns = ["id", "name", "comment"]
        df = pd.DataFrame(output, columns=columns)
        df["id"] = pd.Series(range(df.shape[0]))
        df["label"] = [0 for i in range(df.shape[0])]
        df.dropna(subset=["comment"], inplace=True)
        df.to_csv("output.csv", index=False)
        return df


async def main():
    login_url = "https://www.facebook.com/?stype=lo&deoia=1&jlou=AfczHBzuFgKc5jde3dWHkPnlaB20s2OgvO2xVhdv5IidANHiSADnJtBKCyAvR6aWz5VMH83wtWkYKvxYe9USaIG-fC_7HhCmNfGXIp6jg_Ax3w&smuh=37746&lh=Ac-dfKrOH4QAtVz7HRw"
    post_url = "https://www.facebook.com/langthanghanoiofficial/posts/pfbid0gGc5F6ARLPz4oLSZee9w82Q7KuasUoWX2t4nZDjKpGJWoMkDSVGX1W8zvpLfStWtl"

    scraper = FacebookScraper(login_url, post_url)
    await scraper.scrape()

    output, text = scraper.extract_comment()
    # for o in output:
    #     print(o)

    scraper.save_data(output)

    try:
        scraper.store_to_db(output)
    except Exception as e:
        print("Unable to store data:", e)

    # scraper.visualize_text(text)

if __name__ == "__main__":
    asyncio.run(main())
