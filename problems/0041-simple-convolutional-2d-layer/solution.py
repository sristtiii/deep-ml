import numpy as np

def simple_conv2d(input_matrix: np.ndarray, kernel: np.ndarray, padding: int, stride: int):

    if padding>0:
        input_matrix = np.pad(input_matrix,pad_width= padding , mode ='constant',constant_values =0)

    input_height,input_weight =input_matrix.shape
    kernel_height,kernel_weight = kernel.shape

    # output dimensions 
    width = ((input_weight-kernel_weight)//stride)+1
    height =((input_height-kernel_height)//stride)+1

    output = np.zeros((height,width))

    for i in range(height):
        for j in range(width):

            start_i = i*stride
            start_j = j*stride

            window = input_matrix[start_i:start_i+kernel_height, start_j:start_j+kernel_weight]
            output[i,j]=np.sum(window*kernel)

    return output