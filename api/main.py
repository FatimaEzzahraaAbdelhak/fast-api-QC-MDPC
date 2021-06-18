from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import qcmdpc_core

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/{firstParam}/{secondParam}/{thirdParam}')
async def getCalculer(firstParam, secondParam, thirdParam):
   #kena khadamin f folder dial app lakhra
    # code parameters
    n0 = 2
    r = 5
    wi = 3

    N = 20
    k = r // 2
    #decryption parameters
    t = 1

    ################################## Processing parameters ###################################

    n = n0 * r
    w = wi * n0

    ##################################### Testing functions ####################################

    # generate a random (n,r,w)-QC-MDPC matrix H
    H = qcmdpc_core.genQCMDPC(int(firstParam), int(secondParam), int(thirdParam))

    # Generate the corresponding generator matrix G
    G = qcmdpc_core.genGenQCMDPC(H)
    print("G:\n", G)
    # generate a random message m of weight k
    m = qcmdpc_core.genRandomVector(r, k)

    print("\Texte en clair m:", m)

    # generate a random error vector e of weight t
    e = qcmdpc_core.genRandomVector(n, t)

    # encrypt the message m
    y = qcmdpc_core.encryptMcEliece(G, m, e)

    # decrypt the ciphertext
    decryptedText = qcmdpc_core.demo(H, y.copy())

    # check if decryption is correct
    qcmdpc_core.decryptSuccess(m, decryptedText)


    response = {
        # "genQCMDPC": H.tolist(),
        # "genGenQCMDPC": G.tolist(),
        # "clearText": m.tolist(),
        # "cipherText": y.tolist(),
        # "decryptedText": decryptedText.tolist(),
        # "decrypt_status": decrypt_status
    }
    return response
