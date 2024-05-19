import axiosInstance from "./customize-axios";

const prediction = (inputComment, inputOption) => {
    return axiosInstance.post('/predict/', {
        input_comment: inputComment,
        input_option: inputOption
    });
}

const predict_crawl = (inputLink, inputOption) => {
    return axiosInstance.post('/crawl/', {
        input_Link: inputLink,
        input_option: inputOption
    });
}
export {prediction, predict_crawl};
