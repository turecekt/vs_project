using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using TrouhelnikLib;
namespace TrouhelnikLib
{
    [TestClass]
    public class TrouhelnikTests
    {
        [TestMethod]
        public void Test_AB_7_3_8_9()
        {
            //arrange small values
            double x1 = 7; double y1 = 3; double x2 = 8; double y2 = 9;
            double expected = 6.08;
            double actual = Math.Sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
            actual = Math.Round(actual, 2);
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void Test_AB_4_5_9_7()
        {
            //arrange small values
            double x1 = 4; double y1 = 5; double x2 = 9; double y2 = 7;
            double expected2 = 5.39;
            double actual2 = Math.Sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
            actual2 = Math.Round(actual2, 2);
            Assert.AreEqual(expected2, actual2);
        }

        [TestMethod]
        public void Test_AB_500_11111111_4888888_555555()
        {
            //arrange large values
            double x1 = 500; double y1 = 11111111; double x2 = 4888888; double y2 = 555555;
            double expected = 11632544.85;
            double actual = Math.Sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
            actual = Math.Round(actual, 2);
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void Test_AC_185_45_552_198()
        {
            //arrange
            double x1 = 185; double y1 = 45; double x3 = 552; double y3 = 198;
            double expected = 397.62;
            double actual = Math.Sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3));
            actual = Math.Round(actual, 2);
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void Test_BC_65_99999_552_198()
        {
            //arrange
            double x2 = 65; double y2 = 99999; double x3 = 552; double y3 = 198;
            double expected = 99802.19;
            double actual = Math.Sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3));
            actual = Math.Round(actual, 2);
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void Test_Square_7_3_8_9_10_4()
        {
            double x1 = 7; double y1 = 3; double x2 = 8; double y2 = 9; double x3 = 10; double y3 = 4;
            double expected = 8.5;
            double AB = Math.Sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
            double AC = Math.Sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3));
            double BC = Math.Sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3));
            double s = (AB + AC + BC) / 2;
            double Square = Math.Sqrt(s * (s - AB) * (s - AC) * (s - BC));
            double actual = Math.Round(Square, 2);
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void Test_Perimetr_7_3_8_9_10_4()
        {
            double x1 = 7; double y1 = 3; double x2 = 8; double y2 = 9; double x3 = 10; double y3 = 4;
            double AB = Math.Sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
            double AC = Math.Sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3));
            double BC = Math.Sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3));
            double actual = Math.Round(AB + AC + BC, 2);
            double expected = 14.63;
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void Test_AB_20_3_15_7()
        {
            //arrange small values
            double x1 = 20; double y1 = 3; double x2 = 15; double y2 = 7;
            double expected = 6.4;
            double actual = Math.Sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
            actual = Math.Round(actual, 2);
            Assert.AreEqual(expected, actual);
        }

//0
        [TestMethod]
        public void Test_If_Rectangular_()
        {
            double x1 = 1; double y1 = 1; double x2 = 3; double y2 = 3; double x3 = 3; double y3 = 1;

            double AB = Math.Sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
            double AC = Math.Sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3));
            double BC = Math.Sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3));

            double Hypotinuse = Math.Max(AB, Math.Max(AC, BC));

            double s = (AB + AC + BC) / 2;
            double Square = Math.Sqrt(s * (s - AB) * (s - AC) * (s - BC));
            Square = Math.Round(Square, 2);

            //Určuje pravoúhlý trojúhelník nebo ne
            double katet1 = 0;
            double katet2 = 0;
            bool actual = false;
            bool expected = true;
            if (AB != Hypotinuse) { katet1 = AB; }
            if (AC != Hypotinuse)
            {
                if (katet1 == 0) katet1 = AC;
                else katet2 = AC;
            }
            if (BC != Hypotinuse) { katet2 = BC; }

            if ((katet1 * katet2) / 2 == Square)
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