using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;
using System.Runtime.Serialization.Formatters.Binary;
using System.IO;

public class GameManager : MonoBehaviour {

    public int score;
    public HighScore highScore;

    public Text scoreText;
    public Text highScoreText;

    public string high_score_file_path;


    void Start ()
    {
        high_score_file_path = Application.persistentDataPath + "/high_score.dat";
        score = 0;
        scoreText.text = score.ToString();

        Load();
        highScoreText.text = "Highscore: " + highScore.score.ToString();
	}
	
	void IncreaseScore()
    {
        score += 1;
        scoreText.text = score.ToString();
    }

    void GameOver()
    {
        if (score > highScore.score)
        {
            highScore.score = score;
            highScoreText.text = "Highscore: " + highScore.score.ToString();
        }
        score = 0;
        scoreText.text = score.ToString();
        Save();
    }

    public void Save()
    {
        BinaryFormatter bf = new BinaryFormatter();
        FileStream file = File.Open(high_score_file_path, FileMode.Open);

        bf.Serialize(file, highScore);
        file.Close();

        Debug.Log("Saving Highscore of " + highScore.score.ToString());
    }

    public void Load()
    {
        if (File.Exists(high_score_file_path))
        {
            BinaryFormatter bf = new BinaryFormatter();
            FileStream file = File.Open(high_score_file_path, FileMode.Open);
            highScore = (HighScore)bf.Deserialize(file);
            file.Close();

            Debug.Log("Highscore = " + highScore.score.ToString());
        }
    }
}

[Serializable]
public class HighScore
{
    public Text text;
    public int score;
}