export async function token(){
  var token = await fetch('https://www.universal-tutorial.com/api/getaccesstoken', {
    method: 'GET',
    headers: {
      "Accept": "application/json",
      "api-token": "e2uWgFFOQa7zW452yuNW3MkW9-VBmCqyGGWIsVg5k_bgZ9yvHgko6L4p87akR6kzVMM",
      "user-email": "juanes.malave@gmail.com"
    }
  });
  return await token.json()
}

export async function paises(token){
    var pais = await fetch('https://www.universal-tutorial.com/api/countries', {
      method: 'GET',
      headers: {
        "Authorization": "Bearer "+token,//no toques nada we
        "Accept": "application/json"
      }
    });
    return await pais.json()
  }
  export async function estado(pais,token){
    var estado = await fetch('https://www.universal-tutorial.com/api/states/'+pais, {
      method: 'GET',
      headers: {
        "Authorization": "Bearer "+token,//no toques nada we
        "Accept": "application/json"
      }
    });
    return await estado.json()
  }