// source : https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Utiliser_les_objets

// Parcourir les propriétés d'un objet

function listerToutesLesPropriétés(o){
  var objectToInspect;
  var result = [];
  
  for(objectToInspect = o;
      objectToInspect !== null;
      objectToInspect = Object.getPrototypeOf(objectToInspect)){  
    result = result.concat(Object.getOwnPropertyNames(objectToInspect));  
  }
  return result; 
}
