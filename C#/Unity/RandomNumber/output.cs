using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class output : MonoBehaviour {
    public Text ausgabe;

    private void Awake()
    {
        ausgabe = GetComponent<Text>();
    }


    void Update () {
		if (Zufallszahl.a)
        {
            ausgabe.text = "1";
        }
        else if (Zufallszahl.b)
        {
            ausgabe.text = "2";
        }
        else if (Zufallszahl.c)
        {
            ausgabe.text = "3";
        }
        else if (Zufallszahl.d)
        {
            ausgabe.text = "4";
        }
        else if (Zufallszahl.e)
        {
            ausgabe.text = "5";
        }
        else if (Zufallszahl.f)
        {
            ausgabe.text = "6";
        }
	}
}