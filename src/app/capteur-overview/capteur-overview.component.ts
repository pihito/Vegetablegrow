import { Component, OnInit } from '@angular/core';
import {NodeService} from '../node.service';
import {Node,Capteur} from '../model/capteur';

@Component({
  selector: 'app-capteur-overview',
  templateUrl: './capteur-overview.component.html',
  styleUrls: ['./capteur-overview.component.scss']
})
export class CapteurOverviewComponent implements OnInit {

  nodes : Node[];

  constructor(private nodeService : NodeService) {
   }

  getNode() : void {
     this.nodeService.getNodes()
      .subscribe(nodes => this.nodes = nodes);
  }
  ngOnInit() {
    this.getNode();
  }

}
