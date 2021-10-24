using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class RandomNumber : MonoBehaviour {

    public int zahl;
    public int y = 0;
    public static bool a = false;
    public static bool b = false;
    public static bool c = false;
    public static bool d = false;
    public static bool e = false;
    public static bool f = false;


    public void ChangeNumber()
    {
        a = false;
        b = false;
        c = false;
        d = false;
        e = false;
        f = false;
            System.Random number = new System.Random();
            zahl = number.Next(0, 6);

            if (zahl == 0)
            {
                a = true;
            }
            else if (zahl == 1)
            {
                b = true;
            }
            else if (zahl == 2)
            {
                c = true;
            }
            else if (zahl == 3)
            {
                d = true;
            }
            else if (zahl == 4)
            {
                e = true;
            }
            else
            {
                f = true;
            }
    }
}
