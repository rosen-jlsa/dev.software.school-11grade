using System.Collections.Generic;

public class Repository<T>
{
    private Dictionary <int,T> storage = new Dictionary<int,T>();
    private int nextid = 1;

    public int Add(T item)
    {
        int id = nextid++;
        storage[id] = item;
        return id;
    }
    public T Get(int id)
    {
        return storage[id];
    }
    public bool Remove(int id)
    {
        return storage.Remove(id);
    }
   public List<T> GetAll()
   {
    return new List<T>(storage.Values);
   }

}