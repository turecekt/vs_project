using System;
namespace Test
{
    class Program
    {
        static void Main(string[] args)
        {
            //Testing Marks
            //Program žádá uživatele o zadání souřadnic bodu
            Console.Write($"Enter x for point of triangle A: ");
            double x1 = Convert.ToDouble(Console.ReadLine());
            Console.Write($"Enter y for point of triangle A: ");
            double y1 = Convert.ToDouble(Console.ReadLine());
            Console.Write($"Enter x for point of triangle B: ");
            double x2 = Convert.ToDouble(Console.ReadLine());
            Console.Write($"Enter y for point of triangle B: ");
            double y2 = Convert.ToDouble(Console.ReadLine());
            Console.Write($"Enter x for point of triangle C: ");
            double x3 = Convert.ToDouble(Console.ReadLine());
            Console.Write($"Enter y for point of triangle C: ");
            double y3 = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("_________________________________\n");

            //Určuje délky 3 stran pomocí Pythagorovy věty 
            double AB = Math.Sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
            double AC = Math.Sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3));
            double BC = Math.Sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3));

            //Zavádí dvě proměnné, které budou použity v dalších výpočtech 
            double Square = 0;
            double Perimetr;

            if (AB + AC > BC && AC + BC > AB && BC + AB > AC)
            {
                //Vypisuje souradnice trech pointu
                Console.WriteLine("Triangle exist and has 3 points:\n");                            
                Console.WriteLine($"Point A ({x1},{y1})");
                Console.WriteLine($"Point B ({x2},{y2})");
                Console.WriteLine($"Point C ({x3},{y3})");
                Console.WriteLine("_________________________________\n");

                //Výpočet obvodu trojúhelníku
                Perimetr = (AB + AC + BC);
                Perimetr = Math.Round(Perimetr, 2);
                Console.WriteLine($"Perimeter is\t{Perimetr}");

                //Výpočet plochy trojúhelníku
                double s = (AB + AC + BC) / 2;
                Square = Math.Sqrt(s * (s - AB) * (s - AC) * (s - BC));
                Square = Math.Round(Square, 2);
                Console.WriteLine($"Square is \t{Square}");
                Console.WriteLine("_________________________________\n");

                 //Redukce desetinných míst na dvě
                AB = Math.Round(AB, 2);
                AC = Math.Round(AC, 2);
                BC = Math.Round(BC, 2);       

                //Vypíše délku tří stran
                Console.WriteLine($"AB side has \t{AB} points");
                Console.WriteLine($"AC side has \t{AC} points");
                Console.WriteLine($"BC side has \t{BC} points");
                Console.WriteLine("_________________________________\n");

                //Vypočítá délku nejdelší strany
                double Hypotinuse = Math.Max(AB, Math.Max(AC, BC));
                
                double katet1 = 0;
                double katet2 = 0;

                //Kontroluje zda je trouhelnik pravouhly.
                if (AB != Hypotinuse) { katet1 = AB; }
                if (AC != Hypotinuse)
                {
                    if (katet1 == 0) katet1 = AC;
                    else katet2 = AC;
                }
                if (BC != Hypotinuse) { katet2 = BC; }

                //Vypíše, že trojúhelník není pravoúhlý
                if ((katet1 * katet2) / 2 == Square) 
                {
                    Console.WriteLine("This triangle is rectangular");
                }
                else //Vypíše, že trojúhelník není pravoúhlý
                {    
                    Console.WriteLine("This triangle is not rectangular");
                }
                

            }
            else
            {
                Console.WriteLine("Triangle doesn't exist");
            }
            Console.ReadLine();
        }
    }
}