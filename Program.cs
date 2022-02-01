//-----------------------------------------------------------------------
// <copyright file="Program.cs" company="Pupa-i-Lupa-i-Pupa">
//     Company copyright tag.
// </copyright>
//-----------------------------------------------------------------------

namespace Test
{
    using System;

    /// <summary>
    /// Fulfills all requirements for a triangle project
    /// </summary>
    public class Program
    {
        /// <summary>
        /// Determines whether a triangle exists
        /// </summary>
        public static bool Existing(double ab, double ac, double bc)
        {
            bool isExist = false;
            if (ab + ac >= bc && ac + bc >= ab && bc + ab >= ac && ab != 0 && bc != 0 && ac != 0)
            {
                isExist = true;
            }

            return isExist;
        }

        /// <summary>
        /// Determines whether the triangle is rectangular
        /// </summary>
        public static bool Rectangular(double ab, double ac, double bc)
        {
            bool isRectangular = false;

            // Vypočítá délku nejdelší strany
            double hypotinuse = Math.Max(ab, Math.Max(ac, bc));

            // Výpočet plochy trojúhelníku
            double square;
            double s = (ab + ac + bc) / 2;
            square = Math.Sqrt(s * (s - ab) * (s - ac) * (s - bc));
            square = Math.Round(square, 2);

            // Určuje pravoúhlý trojúhelník nebo ne
            double katet1 = 0;
            double katet2 = 0;
            if (ab != hypotinuse)
            {
                katet1 = ab;
            }

            if (ac != hypotinuse)
            {
                if (katet1 == 0)
                {
                    katet1 = ac;
                }
                else
                {
                    katet2 = ac;
                }
            }

            if (bc != hypotinuse)
            {
                katet2 = bc;
            }

            if ((katet1 * katet2) / 2 == square)
            {
                isRectangular = true;
            }
            else
            {
                isRectangular = false;
            }


            return isRectangular;
        }


        /// <summary>
        /// Uses the above methods. Requires the user to specify the coordinates of the points. Outputs the response.
        /// </summary>
        public static void Main()
        {
            // Testing Marks
            double number;

            // Program žádá uživatele o zadání souřadnic bodu a testuje jestli jich napsal spravne
            double x1 = 0, x2 = 0, x3 = 0, y1 = 0, y2 = 0, y3 = 0;

            Console.Write($"Enter x for point of triangle A: ");
            string temp1 = Console.ReadLine();
            bool isParsable = double.TryParse(temp1, out number);
            if (isParsable)
            {
                x1 = double.Parse(temp1);
            }
            else
            {
                Console.WriteLine("Please enter the correct number");
                Main();
            }

            Console.Write($"Enter y for point of triangle A: ");
            string temp2 = Console.ReadLine();
            isParsable = double.TryParse(temp2, out number);
            if (isParsable)
            {
                y1 = double.Parse(temp2);
            }
            else
            {
                Console.WriteLine("Please enter the correct number");
                Main();
            }

            Console.Write($"Enter x for point of triangle B: ");
            string temp3 = Console.ReadLine();
            isParsable = double.TryParse(temp3, out number);
            if (isParsable)
            {
                x2 = double.Parse(temp3);
            }
            else
            {
                Console.WriteLine("Please enter the correct number");
                Main();
            }

            Console.Write($"Enter y for point of triangle B: ");
            string temp4 = Console.ReadLine();
            isParsable = double.TryParse(temp4, out number);
            if (isParsable)
            {
                y2 = double.Parse(temp4);
            }
            else
            {
                Console.WriteLine("Please enter the correct number");
                Main();
            }

            Console.Write($"Enter x for point of triangle C: ");
            string temp5 = Console.ReadLine();
            isParsable = double.TryParse(temp5, out number);
            if (isParsable)
            {
                x3 = double.Parse(temp5);
            }
            else
            {
                Console.WriteLine("Please enter the correct number");
                Main();
            }

            Console.Write($"Enter y for point of triangle C: ");
            string temp6 = Console.ReadLine();
            isParsable = double.TryParse(temp6, out number);
            if (isParsable)
            {
                y3 = double.Parse(temp6);
            }
            else
            {
                Console.WriteLine("Please enter the correct number");
                Main();
            }

            Console.WriteLine("_________________________________\n");

            // Určuje délky 3 stran pomocí Pythagorovy věty 
            double ab = Math.Sqrt(((x1 - x2) * (x1 - x2)) + ((y1 - y2) * (y1 - y2)));
            double ac = Math.Sqrt(((x1 - x3) * (x1 - x3)) + ((y1 - y3) * (y1 - y3)));
            double bc = Math.Sqrt(((x2 - x3) * (x2 - x3)) + ((y2 - y3) * (y2 - y3)));

            // Zavádí dvě proměnné, které budou použity v dalších výpočtech 
            double square;
            double perimetr;

            if (Existing(ab, ac, bc))
            {
                // Vypisuje souradnice trech pointu
                Console.WriteLine("Triangle exist and has 3 points:\n");
                Console.WriteLine($"Point A ({x1},{y1})");
                Console.WriteLine($"Point B ({x2},{y2})");
                Console.WriteLine($"Point C ({x3},{y3})");
                Console.WriteLine("_________________________________\n");

                // Výpočet obvodu trojúhelníku
                perimetr = ab + ac + bc;
                perimetr = Math.Round(perimetr, 2);
                Console.WriteLine($"Perimeter is\t{perimetr}");

                // Výpočet plochy trojúhelníku
                double s = (ab + ac + bc) / 2;
                square = Math.Sqrt(s * (s - ab) * (s - ac) * (s - bc));
                square = Math.Round(square, 2);
                Console.WriteLine($"Square is \t{square}");
                Console.WriteLine("_________________________________\n");

                // Redukce desetinných míst na dvě
                ab = Math.Round(ab, 2);
                ac = Math.Round(ac, 2);
                bc = Math.Round(bc, 2);

                // Vypíše délku tří stran
                Console.WriteLine($"AB side has \t{ab} points");
                Console.WriteLine($"AC side has \t{ac} points");
                Console.WriteLine($"BC side has \t{bc} points");
                Console.WriteLine("_________________________________\n");

                if (Rectangular(ab, ac, bc))
                {
                    Console.WriteLine("This triangle is rectangular");
                }
                else
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