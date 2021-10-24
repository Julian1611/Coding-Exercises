using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerSteering : MonoBehaviour
{
    public Rigidbody rb;
    public float speed;

    public static Vector3 mousePosition;
    public Vector3 targetM;
    public Vector3 start;
    public Transform targetR;

    private void Start()
    {
        rb = GetComponent<Rigidbody>();
    }

    private void Update()
    {
        if (Input.GetMouseButton(0))
        {
            mousePosition = Input.mousePosition;

            

            Vector3 relativePos = targetR.position - transform.position;
            Quaternion rotation = Quaternion.LookRotation(relativePos);
            transform.rotation = rotation;

            mousePosition.z = 45;
            mousePosition = Camera.main.ScreenToWorldPoint(mousePosition);
        }
        transform.position = Vector3.Lerp(transform.position, mousePosition, speed * Time.deltaTime);
    }
}

public class Rotation : MonoBehaviour {

    public Transform this_;

    private void LateUpdate()
    {
        this_.position = PlayerSteering.mousePosition;
    }
}

public class CameraMovement : MonoBehaviour
{
    public Rigidbody rb;
    public float speed;

    public float horizontalSpeed = 2;
    public float verticalSpeed = 2;
    public Transform me;

    private void Start()
    {
        rb = GetComponent<Rigidbody>();
    }

    private void FixedUpdate()
    {
        /*float moveHorizontal = Input.GetAxis("Horizontal");
        float moveVertical = Input.GetAxis("Vertical");


        Vector3 movement = new Vector3(0.0f, 0.0f, moveVertical);
        rb.velocity = movement * speed;

        if (Input.GetMouseButton(0))
        {
            float h = horizontalSpeed * Input.GetAxis("Mouse Y");
            float v = verticalSpeed * Input.GetAxis("Mouse X");
            me.Translate(v, h, 0);
        }*/
    }
}