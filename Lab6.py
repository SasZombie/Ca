import numpy as np
import matplotlib.pyplot as plt


def main()->None:
    list1=[1.4,5.9,2.6,7.3,8.5,9.3,6.1]
    num_arr = np.array(list1)
    print(num_arr)
    
    even_numbers = np.arange(70, 92, 2)
    print(even_numbers)

    matrix = np.zeros((3, 3), dtype=int)
    matrix = np.diag([3, 7, 11])
    
    print(matrix)
    
    array = np.arange(10, 16).reshape(2, 3)
    print(array)
    
    ex5=np.array([[10,50,70,20,40],[5,45,95,35,65]])
    
    
    print(ex5 [ex5 < 43])
    
    print(ex5 [ex5 > 43])

    np.save('data.npy', ex5)
    
    ex6 = np.load('data.npy')
    
    print(ex6)

    x = np.linspace(0, 10, 100)
    y = np.tan(x)

    fig, axes = plt.subplots(3, 2, figsize=(10, 12))

    axes[0, 0].plot(x, y, marker='o', markerfacecolor='red', linestyle='-')
    axes[0, 0].set_title('Line with Custom Marker Color')

    axes[0, 1].plot(x, y, linestyle=':', color='green')
    axes[0, 1].grid(True)
    axes[0, 1].set_title('Line with Custom Style and Grid')

    axes[1, 0].bar(x, y, color='pink', width=0.5)
    axes[1, 0].set_title('Vertical Bars with Custom Color and Width')

    scatter_colors = np.random.rand(len(x))
    axes[1, 1].scatter(x, y, c=scatter_colors, cmap='viridis')
    axes[1, 1].set_title('Scattered Points with Different Colors')

    axes[2, 0].plot(x, y, linestyle='-.', color='red', label='Line 1')
    axes[2, 0].plot(x, -y, linewidth=2, color='blue', label='Line 2')
    axes[2, 0].legend()
    axes[2, 0].set_title('Lines with Custom Style, Color, and Width')

    axes[2, 1].barh(x, y, color='pink', height=0.2)
    axes[2, 1].set_title('Horizontal Bars with Custom Color and Height')

    plt.tight_layout()
    plt.show()
    

if __name__ == '__main__':
    main()