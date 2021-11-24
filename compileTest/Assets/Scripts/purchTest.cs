using System.Collections;
using System.Collections.Generic;
using System.Net;
using UnityEngine;

public class pTest  {

    public void fun()
    {
        ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };
    }
}
