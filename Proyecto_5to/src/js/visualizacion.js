export default async function data(correo){
  

    var token = await fetch('http://localhost:9000/consulta_todo/', {
      method: 'POST',
      headers: {
        "Content-Type": "application/json"
      },
      body:{
        correo: correo.correo
        }
    });
    return await token.json()
  }