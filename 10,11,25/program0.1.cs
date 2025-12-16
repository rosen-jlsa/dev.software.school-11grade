using System.Collections.Generic;

public static int[] FileArray(int[] array, int threshold)
{
    List<int> result = new List<int>();
    foreach (int item in array)
    {
    if(item > threshold)
    {
        result.Add(item);
    }

    }
    return result.ToArray();
}