# DATASET ban đầu
* Tập train:  12500 images của chó, 12500 images của mèo.
* Tập test:   12500 images của chó và mèo.
* Kích thước: mỗi bức ảnh có kích thước khác nhau.
# Vấn đề đặt ra
* Vì số lượng DATASET ban đầu quá lớn, đồng thời kích thước các images không giống nhau.
* Hướng giải quết: Chọn ra một số lượng images nhất định, đồng thời Resize ảnh lại theo nhu cầu.
# DATASET sau khi xử lý
* Tập train:  50 images của chó, 12500 images của mèo.
* Tập test:   50 images của chó và mèo.
* Kích thước: 28x28x3

# Cây thư mục
* Dataset
* * TrainSample
* * * Cats
* * * * Images
* * * * ResizedIma
* * * Dogs
* * TestSample
* * * Cats
* * * Dogs
