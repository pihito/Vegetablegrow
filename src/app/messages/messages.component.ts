import { Component, OnInit } from '@angular/core';

import {Alert, ALERTS} from '../model/messageAlert'
import { MessageService } from '../message.service';

@Component({
  selector: 'app-messages',
  templateUrl: './messages.component.html',
  styleUrls: ['./messages.component.scss']
})
export class MessagesComponent implements OnInit {

  alerts: Alert[];

  constructor(public messageService: MessageService) {
    this.reset();
  }
   

  close(alert: Alert) {
    this.alerts.splice(this.alerts.indexOf(alert), 1);
  }

  reset() {
    this.alerts = Array.from(ALERTS);
  }

  ngOnInit() {
  }

}