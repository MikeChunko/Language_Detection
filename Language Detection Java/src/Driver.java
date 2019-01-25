// Michael Chunko
// Mr. Gill
// CS4
// 2018

// The driver for doing all of the preprocessing
public class Driver {
    public static void main(String[] args) {
        Preprocessing.prepareData("D:/Mike/Documents/NeuralNetworkData/train-raw-de.txt",
                "D:/Mike/Documents/NeuralNetworkData/train-de.txt", "0");

        Preprocessing.prepareData("D:/Mike/Documents/NeuralNetworkData/train-raw-en.txt",
                "D:/Mike/Documents/NeuralNetworkData/train-en.txt", "1");

        Preprocessing.prepareData("D:/Mike/Documents/NeuralNetworkData/train-raw-es.txt",
                "D:/Mike/Documents/NeuralNetworkData/train-es.txt", "2");

        Preprocessing.prepareData("D:/Mike/Documents/NeuralNetworkData/train-raw-it.txt",
                "D:/Mike/Documents/NeuralNetworkData/train-it.txt", "3");

        Preprocessing.prepareData("D:/Mike/Documents/NeuralNetworkData/test-raw-de.txt",
                "D:/Mike/Documents/NeuralNetworkData/test-de.txt", "0");

        Preprocessing.prepareData("D:/Mike/Documents/NeuralNetworkData/test-raw-en.txt",
                "D:/Mike/Documents/NeuralNetworkData/test-en.txt", "1");

        Preprocessing.prepareData("D:/Mike/Documents/NeuralNetworkData/test-raw-es.txt",
                "D:/Mike/Documents/NeuralNetworkData/test-es.txt", "2");

        Preprocessing.prepareData("D:/Mike/Documents/NeuralNetworkData/test-raw-it.txt",
                "D:/Mike/Documents/NeuralNetworkData/test-it.txt", "3");
    }
}