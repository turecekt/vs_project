//-----------------------------------------------------------------------
// <copyright file="TrouhelnikTests.cs" company="Pupa-i-Lupa-i-Pupa">
//     Company copyright tag.
// </copyright>
//-----------------------------------------------------------------------

namespace TrouhelnikLib
{
    using System;
    using Microsoft.VisualStudio.TestTools.UnitTesting;
    using Test;

    /// <summary>
    /// The class checks the correctness of the solution with my values
    /// </summary>
    [TestClass]
    public class TrouhelnikTests
    {
        /// <summary>
        /// Test the triangle with points: 7_3_8_9
        /// </summary>
        [TestMethod]
        public void Test_AB_7_3_8_9()
        {
            // arrange
            double x1 = 7;
            double y1 = 3;
            double x2 = 8;
            double y2 = 9;
            double expected = 6.08;
            double actual = Math.Sqrt(((x1 - x2) * (x1 - x2)) + ((y1 - y2) * (y1 - y2)));
            actual = Math.Round(actual, 2);
            Assert.AreEqual(expected, actual);
        }

        /// <summary>
        /// Test if the triangle exist with positive answer
        /// </summary>
        [TestMethod()]
        public void ExistingTest_True()
        {
            bool isExist = Program.Existing(5, 10, 11.18);
            Assert.IsTrue(isExist);
        }

        /// <summary>
        /// Test if the triangle exist negative answer
        /// </summary>
        [TestMethod()]
        public void ExistingTest_false()
        {
            bool isExist = Program.Existing(0, 0, 0);
            Assert.IsTrue(!isExist);
        }

        /// <summary>
        /// Test if the triangle is rectangulare with positive answer
        /// </summary>
        [TestMethod()]
        public void RectagularTest_True()
        {
            bool isRectangular = Program.Rectangular(5, 10, 11.18);
            Assert.IsTrue(isRectangular);
        }

        /// <summary>
        /// Test if the triangle is rectangulare with negative answer
        /// </summary>
        [TestMethod()]
        public void RectagularTest_false()
        {
            bool isRectangular = Program.Rectangular(5, 12.21, 10.2);
            Assert.IsTrue(!isRectangular);
        }

        /// <summary>
        /// Test the triangle with points: 4_5_9_7
        /// </summary>
        [TestMethod]
        public void Test_AB_4_5_9_7()
        {
            // arrange
            double x1 = 4;
            double y1 = 5;
            double x2 = 9;
            double y2 = 7;
            double expected2 = 5.39;
            double actual2 = Math.Sqrt(((x1 - x2) * (x1 - x2)) + ((y1 - y2) * (y1 - y2)));
            actual2 = Math.Round(actual2, 2);
            Assert.AreEqual(expected2, actual2);
        }

        /// <summary>
        /// Test the triangle with points: 500_11111111_4888888_555555
        /// </summary>
        [TestMethod]
        public void Test_AB_500_11111111_4888888_555555()
        {
            // arrange
            double x1 = 500;
            double y1 = 11111111;
            double x2 = 4888888;
            double y2 = 555555;
            double expected = 11632544.85;
            double actual = Math.Sqrt(((x1 - x2) * (x1 - x2)) + ((y1 - y2) * (y1 - y2)));
            actual = Math.Round(actual, 2);
            Assert.AreEqual(expected, actual);
        }

        /// <summary>
        /// Test the triangle with points: 185_45_552_198
        /// </summary>
        [TestMethod]
        public void Test_AC_185_45_552_198()
        {
            // arrange
            double x1 = 185;
            double y1 = 45;
            double x3 = 552;
            double y3 = 198;
            double expected = 397.62;
            double actual = Math.Sqrt(((x1 - x3) * (x1 - x3)) + ((y1 - y3) * (y1 - y3)));
            actual = Math.Round(actual, 2);
            Assert.AreEqual(expected, actual);
        }

        /// <summary>
        /// Test the triangle with points: 65_99999_552_198
        /// </summary>
        [TestMethod]
        public void Test_BC_65_99999_552_198()
        {
            // arrange
            double x2 = 65;
            double y2 = 99999;
            double x3 = 552;
            double y3 = 198;
            double expected = 99802.19;
            double actual = Math.Sqrt(((x2 - x3) * (x2 - x3)) + ((y2 - y3) * (y2 - y3)));
            actual = Math.Round(actual, 2);
            Assert.AreEqual(expected, actual);
        }

        /// <summary>
        /// Test the triangle Square
        /// </summary>
        [TestMethod]
        public void Test_Square_7_3_8_9_10_4()
        {
            double x1 = 7;
            double y1 = 3;
            double x2 = 8;
            double y2 = 9;
            double x3 = 10;
            double y3 = 4;
            double expected = 8.5;
            double ab = Math.Sqrt(((x1 - x2) * (x1 - x2)) + ((y1 - y2) * (y1 - y2)));
            double ac = Math.Sqrt(((x1 - x3) * (x1 - x3)) + ((y1 - y3) * (y1 - y3)));
            double bc = Math.Sqrt(((x2 - x3) * (x2 - x3)) + ((y2 - y3) * (y2 - y3)));
            double s = (ab + ac + bc) / 2;
            double square = Math.Sqrt(((s * (s - ab)) * (s - ac)) * (s - bc));
            double actual = Math.Round(square, 2);
            Assert.AreEqual(expected, actual);
        }

        /// <summary>
        /// Test the triangle with points: 7_3_8_9_10_4
        /// </summary>
        [TestMethod]
        public void Test_Perimetr_7_3_8_9_10_4()
        {
            double x1 = 7;
            double y1 = 3;
            double x2 = 8;
            double y2 = 9;
            double x3 = 10;
            double y3 = 4;
            double ab = Math.Sqrt(((x1 - x2) * (x1 - x2)) + ((y1 - y2) * (y1 - y2)));
            double ac = Math.Sqrt(((x1 - x3) * (x1 - x3)) + ((y1 - y3) * (y1 - y3)));
            double bc = Math.Sqrt(((x2 - x3) * (x2 - x3)) + ((y2 - y3) * (y2 - y3)));
            double actual = Math.Round(ab + ac + bc, 2);
            double expected = 14.63;
            Assert.AreEqual(expected, actual);
        }

        /// <summary>
        /// Test if the triangle is Rectangular
        /// </summary>
        [TestMethod]
        public void Test_If_Rectangular_()
        {
            double x1 = 1;
            double y1 = 1;
            double x2 = 3;
            double y2 = 3;
            double x3 = 3;
            double y3 = 1;

            double ab = Math.Sqrt(((x1 - x2) * (x1 - x2)) + ((y1 - y2) * (y1 - y2)));
            double ac = Math.Sqrt(((x1 - x3) * (x1 - x3)) + ((y1 - y3) * (y1 - y3)));
            double bc = Math.Sqrt(((x2 - x3) * (x2 - x3)) + ((y2 - y3) * (y2 - y3)));

            double hypotinuse = Math.Max(ab, Math.Max(ac, bc));

            double s = (ab + ac + bc) / 2;
            double square = Math.Sqrt(((s * (s - ab)) * (s - ac)) * (s - bc));
            square = Math.Round(square, 2);

            // Určuje pravoúhlý trojúhelník nebo ne
            double katet1 = 0;
            double katet2 = 0;
            bool actual = false;
            bool expected = true;
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
                actual = true;
            }
            else
            {
                actual = false;
            }

            Assert.AreEqual(expected, actual);
        }
    }
}