using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
using System;
using System.Runtime.Serialization.Formatters.Binary;
using System.IO;

public class Settings : MonoBehaviour {

    public static bool white;
    public static bool black;
    public string background_color_file_path;
    public BackgroundColor whiteTrue;

    public Color whiteC;
    public Color blackC;

    public Image button1;
    public Image button2;
    public Text text1;
    public Text text2;

    public GameObject Pic1;
    public GameObject Pic2;

    public Camera cam;

    private void Start()
    {
        background_color_file_path = Application.persistentDataPath + "/white_bool.dat";

        cam.clearFlags = CameraClearFlags.SolidColor;

        /*if (!white && !black)
        {
            white = false;

            Pic1.SetActive(true);
            Pic2.SetActive(false);
        }*/

        Load();

        if (whiteTrue.white)
        {
            white = true;
            black = false;
        }
        else if (!whiteTrue.white)
        {
            white = false;
            black = true;
        }
    }

    public void StartGame()
    {
        SceneManager.LoadScene(1);
    }

    public void BackgroundColorChange()
    {
        if (!white)
        {
            white = true;
            black = false;

            whiteTrue.white = true;

            cam.backgroundColor = whiteC;

            button1.color = whiteC;
            text1.color = blackC;
            button2.color = whiteC;
            text2.color = blackC;

            Pic2.SetActive(false);
            Pic1.SetActive(true);
        }
        else if (!black)
        {
            black = true;
            white = false;

            whiteTrue.white = false;

            cam.backgroundColor = blackC;

            button1.color = blackC;
            text1.color = whiteC;
            button2.color = blackC;
            text2.color = whiteC;

            Pic1.SetActive(false);
            Pic2.SetActive(true);
        }

        Save();
    }

    public void Save()
    {
        BinaryFormatter bf = new BinaryFormatter();
        FileStream file = File.Create(background_color_file_path);

        bf.Serialize(file, whiteTrue);
        file.Close();
    }

    public void Load()
    {
        if (File.Exists(background_color_file_path))
        {
            BinaryFormatter bf = new BinaryFormatter();
            FileStream file = File.Open(background_color_file_path, FileMode.Open);
            whiteTrue = (BackgroundColor)bf.Deserialize(file);
            file.Close();
        }
    }
}

[Serializable]
public class BackgroundColor
{
    public bool white;
}