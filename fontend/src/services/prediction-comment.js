import axiosInstance from "./customize-axios";

const prediction = (inputComment, inputOption) => {
    return axiosInstance.post('/predict/', {
        input_comment: inputComment,
        input_option: inputOption
    });
}
export {prediction};
