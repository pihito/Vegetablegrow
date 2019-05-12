import { Injectable } from '@angular/core';


import {Alert, ALERTS} from './model/messageAlert'

@Injectable({
  providedIn: 'root'
})
export class MessageService {

  alerts = ALERTS;
 
  add(message: Alert) {
    this.alerts.push(message);
  }
 
  supp(message: Alert) {
    this.alerts.splice(this.alerts.indexOf(message), 1);
  }

  clear() {
    this.alerts = [];
  }
  
  constructor() { }

}
