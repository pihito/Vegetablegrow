export class Node {
    id: number;
    name: string;
    type: number;
    capteurs : Capteur[];
  }

  export class Capteur {
    id : number;
    valeur : number;
    unite : string;
    nom : string;

  }

export const NODES : Node[] = [{
    id: 1,
    name: 'cuisine',
    type: 1,
    capteurs :[
        {
            id : 1,
            valeur : 30,
            nom : 'humidité',
            unite : '%'
        },{
            id : 2,
            valeur : 22,
            nom : 'temperature',
            unite : '°C'
        },{
            id : 3,
            valeur : 150,
            nom : 'lumière',
            unite : '°C'
        }
    ]},{
    id: 2,
    name: 'salon',
    type: 1,
    capteurs :  [
        {
            id : 1,
            valeur : 30,
            nom : 'humidité',
            unite : '%'
        },{
            id : 2,
            valeur : 22,
            nom : 'temperature',
            unite : '°C'
        },{
            id : 3,
            valeur : 150,
            nom : 'lumière',
            unite : '°C'
        }
    ]},{
    id: 3,
    name: 'chambre',
    type: 1,
    capteurs :  [
        {
            id : 1,
            valeur : 30,
            nom : 'humidité',
            unite : '%'
        },{
            id : 2,
            valeur : 22,
            nom : 'temperature',
            unite : '°C'
        },{
            id : 3,
            valeur : 150,
            nom : 'lumière',
            unite : '°C'
        }
    ]
}];