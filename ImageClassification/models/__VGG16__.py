from torch import nn

class VGG16(nn.Module):
    def __init__(self, num_classes):
        super(VGG16,self).__init__()
        self.sequential_224 = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3, padding='same'), nn.ReLU(),
            nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, padding='same'), nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        self.sequential_112 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, padding='same'), nn.ReLU(),
            nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, padding='same'), nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        self.sequential_56 = nn.Sequential(
            nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, padding='same'), nn.ReLU(),
            nn.Conv2d(in_channels=256, out_channels=256, kernel_size=3, padding='same'), nn.ReLU(),
            nn.Conv2d(in_channels=256, out_channels=256, kernel_size=3, padding='same'), nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        self.sequential_28 = nn.Sequential(
            nn.Conv2d(in_channels=256, out_channels=512, kernel_size=3, padding='same'), nn.ReLU(),
            nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, padding='same'), nn.ReLU(),
            nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, padding='same'), nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        self.sequential_14 = nn.Sequential(
            nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, padding='same'), nn.ReLU(),
            nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, padding='same'), nn.ReLU(),
            nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, padding='same'), nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        self.sequential_linear = nn.Sequential(
            nn.Flatten(),
            nn.Linear(in_features=512*7*7, out_features=4096), nn.ReLU(),
            nn.Linear(in_features=4096, out_features=4096), nn.ReLU(),
            nn.Linear(in_features=4096, out_features=num_classes), nn.ReLU(),
            nn.Softmax()
        )

    def forward(self,x):
        x = self.sequential_224(x)
        x = self.sequential_112(x)
        x = self.sequential_56(x)
        x = self.sequential_28(x)
        x = self.sequential_14(x)
        x = self.sequential_linear(x)
        return x