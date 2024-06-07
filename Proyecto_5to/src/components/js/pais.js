export async function paises(){
    var pais = await fetch('https://www.universal-tutorial.com/api/countries', {
      method: 'GET',
      headers: {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7InVzZXJfZW1haWwiOiJqdWFubWFsYXZlLml0am9AZ21haWwuY29tIiwiYXBpX3Rva2VuIjoiaEpTZzJwVFkyMUhMZHJKaHNxRE5Fcldhd0xFVFBCdDJLQ25odjVabGw1b29qc2NPM3J5TUYwZ05XbmtMa0ptWDZJYyJ9LCJleHAiOjE3MTc4ODgyMjl9.E5BSvZBnir7ZgzAbGYOUQe4Srx0fE7f3S5IhRcjwT1Y",//no toques nada we
        "Accept": "application/json"
      }
    });
    return await pais.json()
  }
  export async function estado(pais){
    var estado = await fetch('https://www.universal-tutorial.com/api/states/'+pais, {
      method: 'GET',
      headers: {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7InVzZXJfZW1haWwiOiJqdWFubWFsYXZlLml0am9AZ21haWwuY29tIiwiYXBpX3Rva2VuIjoiaEpTZzJwVFkyMUhMZHJKaHNxRE5Fcldhd0xFVFBCdDJLQ25odjVabGw1b29qc2NPM3J5TUYwZ05XbmtMa0ptWDZJYyJ9LCJleHAiOjE3MTc4ODgyMjl9.E5BSvZBnir7ZgzAbGYOUQe4Srx0fE7f3S5IhRcjwT1Y",//no toques nada we
        "Accept": "application/json"
      }
    });
    return await estado.json()
  }