using System;

namespace ConsoleMVC.Models
{
    public class Tip
    {
        private double amount;
        private double percent;

        public double Amount
        {
            get { return amount; }
            set { amount = value; }
        }

        public double Percent
        {
            get { return percent; }
            set
            {
                if (value > 1)
                {
                    percent = value / 100.0;
                }
                else
                {
                    percent = value;
                }
            }
        }

        public Tip() : this(0, 0) { }

        public Tip(double amount, double percent)
        {
            Amount = amount;
            Percent = percent;
        }

        public double CalculateTip()
        {
            return Amount * Percent;
        }

        public double CalculateTotal()
        {
            return Amount + CalculateTip();
        }
    }
}