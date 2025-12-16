public class Car
{
    private string brand;
    private int year;

    
    public Car()
    {
        brand = "Unknown"; // 2 т. 
        year = 0; // 2 т. 
    }

    
    public Car(string brand, int year) // 4 т. 
        this.year = year;
    }

    
    public void PrintInfo() // 6 т.
    {
        Console.WriteLine($"Car: {brand}, Year: {year}"); 
    }

    
    public bool IsOld() // 6 т.
    {
        return year < 2000; 
    }


class Program
{
    static void Main()
    {
        Car c1 = new Car(); // Expected: Unknown, 0
        Car c2 = new Car("Toyota", 1999); // Expected: Toyota, 1999

        c1.PrintInfo(); // 5 т. (ако отпечата точно "Car: Unknown, Year: 0")
        c2.PrintInfo(); // 3 т.
        Console.WriteLine(c2.IsOld()); // 2 т. (true)
    }
}