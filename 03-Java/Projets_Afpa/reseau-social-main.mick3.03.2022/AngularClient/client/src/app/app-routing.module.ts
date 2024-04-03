import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {CreationComponent} from "./creation/creation.component";
import {AppComponent} from "./app.component";
import {HomeComponent} from "./home/home.component";
import {ConnectionComponent} from "./connection/connection.component";

const routes: Routes = [
  {path: "", component: HomeComponent},
  {path: "home", redirectTo: ""},
  {path: "creation", component:CreationComponent},
  {path: "connection", component:ConnectionComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
