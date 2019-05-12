import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';

import{ MessageService} from './message.service';
import {Node,Capteur,NODES} from './model/capteur';
import {Alert} from './model/messageAlert';


@Injectable({
  providedIn: 'root'
})
export class NodeService {

  constructor(private messageService :MessageService) { }

  getNodes() : Observable<Node[]> {
    let alert = new Alert();
    alert.type = 'success';
    alert.message = 'get all nodes';
    this.messageService.add(alert);
    return of (NODES);
  }
}
