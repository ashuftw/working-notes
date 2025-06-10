---
title: Neural Network Formulae for Calculations
draft: true
tags: 
date: 2025-04-22
---
**Total Parameters in a Fully Connected Layer**
(input_dimensions × neurons_in_layer) + neurons_in_layer  

Example:
- Input: 100 dimensions
- Output: 10 neurons
- Weights: 100 × 10 = 1000 parameters (each input connects to each neuron)
- Biases: 10 (one bias per neuron)
- Total: 1000 + 10 = 1010 parameters

**Total Parameters in a Convolutional layer with $n$ kernels**
(input_channels × kernel_height × kernel_width  × num_kernels) + num_kernels

*First term represents weights, second term represents biases*

> For a convolutional layer processing an image:
> - **Input channels** refers to the depth of the input volume (e.g., 3 for RGB images, 1 for grayscale)
> - This is because the in a CNN, the entire image (2D Plane) is processed separately and combined through filters. 
> 
> For a fully connected layer:
> - There's no concept of "channels" - everything is flattened into a single vector

**Output Dimensions of a Convolutional layer**
- Output height = ⌊(Input height - kernel height + 2$\times$padding)/stride_v + 1⌋
- Output width = ⌊(Input width - kernel width + 2$\times$padding)/stride_h + 1⌋

For pooling layers:

- Output height = ⌊(Input height - pool size + 2$\times$padding)/stride_v + 1⌋
- Output width = ⌊(Input width - pool size + 2$\times$padding)/stride_h + 1⌋    

> Note: The floor function, denoted as ⌊x⌋ or floor(x), rounds a number down to the nearest integer that is less than or equal to the original number. ⌊3.7⌋ = 3, ⌊-7.9⌋ = -8