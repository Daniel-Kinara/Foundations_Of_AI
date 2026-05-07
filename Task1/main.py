import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt

# Convert images to tensors
transform = transforms.ToTensor()

# Download dataset
train_dataset = torchvision.datasets.MNIST(
    root="./data", train=True, download=True, transform=transform
)

# Get one image
image, label = train_dataset[0]

# Show image
plt.imshow(image.squeeze(), cmap="gray")

# Title
plt.title(f"Label: {label}")

# Display
plt.show()
