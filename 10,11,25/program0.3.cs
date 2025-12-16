using System;

public interface IPrintable<T>
{
    void Print(T item);
}
public class PersonPrinter :  IPrintable<Person>
{
    public void Print(Person person)
    {
        Console.WriteLine($"Name: {person.Name}, Age: {person.Age}");
    }
}
public class Person 
{
public string Name { get; set; }
public int Age { get; set; }
}