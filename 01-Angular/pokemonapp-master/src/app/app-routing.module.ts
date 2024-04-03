import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {PokemonsViewComponent} from "./pokemons/pokemons-view/pokemons-view.component";
import {PokemonDetailsComponent} from "./pokemons/pokemon-details/pokemon-details.component";
import {CurrencyAppComponent} from "./currency-exchange/currency-view/app.component";
import {HomeComponent} from "./_home/home.component";
import {BanqueAppComponent} from "./banque/banque-view/banque-view.component";
import {NewAccountComponent} from "./banque/new-account/new-account.component";
import {TransferComponent} from "./banque/transfer/transfer.component";

const routes: Routes = [
  {path: "", component:HomeComponent},
  {path: "pokemons", component:PokemonsViewComponent},
  {path: "pokemons/:id", component:PokemonDetailsComponent},
  {path: "currency", component:CurrencyAppComponent},
  {path: "banque", component:BanqueAppComponent},
  {path: "banque/new", component:NewAccountComponent},
  {path: "banque/transfer", component:TransferComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
