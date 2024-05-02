using UnityEngine;

public class RotatingCylinder : MonoBehaviour
{
    public Transform cylinderTransform; // Referencia al transform del cilindro
    public float angularVelocity = 10f; // Velocidad angular inicial del cilindro

    private void Update()
    {
        // Rotación del cilindro
        cylinderTransform.Rotate(Vector3.up * angularVelocity * Time.deltaTime);
    }
}
using UnityEngine;

public class AluminumCan : MonoBehaviour
{
    public Transform canTransform; // Referencia al transform de la lata
    public float frictionCoefficient = 0.5f; // Coeficiente de fricción estática entre la lata y el cilindro

    private void OnTriggerStay(Collider other)
    {
        if (other.CompareTag("Cylinder"))
        {
            // Calcula la fuerza de fricción estática
            Vector3 frictionForce = -canTransform.right * frictionCoefficient * Physics.gravity.magnitude;

            // Aplica la fuerza de fricción a la lata
            canTransform.GetComponent<Rigidbody>().AddForce(frictionForce, ForceMode.Force);
        }
    }
}
using UnityEngine;

public class ExperimentController : MonoBehaviour
{
    public RotatingCylinder cylinder; // Referencia al cilindro rotatorio
    public AluminumCan aluminumCan; // Referencia a la lata de aluminio
    public float minAngularVelocity = 1f; // Velocidad angular mínima inicial
    public float maxAngularVelocity = 20f; // Velocidad angular máxima
    public float velocityIncrement = 1f; // Incremento de velocidad angular por iteración

    private float currentAngularVelocity;

    private void Start()
    {
        currentAngularVelocity = minAngularVelocity;
    }

    private void Update()
    {
        // Actualiza la velocidad angular del cilindro
        cylinder.angularVelocity = currentAngularVelocity;

        // Si la lata de aluminio no está en contacto con el cilindro, aumenta la velocidad angular
        if (!IsCanOnCylinder())
        {
            currentAngularVelocity += velocityIncrement;
            // Si hemos excedido la velocidad angular máxima, detenemos la experimentación
            if (currentAngularVelocity > maxAngularVelocity)
            {
                Debug.Log("La lata se ha caído. Velocidad angular mínima necesaria: " + (currentAngularVelocity - velocityIncrement));
                enabled = false; // Desactiva este script
            }
        }
    }

    private bool IsCanOnCylinder()
    {
        // Comprueba si la lata está en contacto con el cilindro
        Collider[] colliders = Physics.OverlapBox(aluminumCan.canTransform.position, aluminumCan.canTransform.localScale / 2f, aluminumCan.canTransform.rotation);
        foreach (Collider collider in colliders)
        {
            if (collider.CompareTag("Cylinder"))
            {
                return true;
            }
        }
        return false;
    }
}
