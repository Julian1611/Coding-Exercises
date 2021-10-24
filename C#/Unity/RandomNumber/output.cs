using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class output : MonoBehaviour {
    public Text ausgabe;

    private void Awake()
    {
        out = GetComponent<Text>();
    }


    void Update () {
		if (RandomNumber.a)
        {
            out.text = "1";
        }
        else if (RandomNumber.b)
        {
            out.text = "2";
        }
        else if (RandomNumber.c)
        {
            out.text = "3";
        }
        else if (RandomNumber.d)
        {
            out.text = "4";
        }
        else if (RandomNumber.e)
        {
            out.text = "5";
        }
        else if (RandomNumber.f)
        {
            out.text = "6";
        }
	}
}
