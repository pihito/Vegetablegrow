import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AdminComponent} from './admin/admin.component';
import { CapteurOverviewComponent } from "./capteur-overview/capteur-overview.component";

const routes: Routes = [
  { path: 'admin', component: AdminComponent},
  { path: 'overview', component: CapteurOverviewComponent }, 
  { path: '', redirectTo: '/overview', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
