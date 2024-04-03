import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PokemonDetailsComponent } from './pokemons/pokemon-details/pokemon-details.component';
import { BorderCardDirective } from './pokemons/border-card.directive';
import { PokemonsViewComponent } from './pokemons/pokemons-view/pokemons-view.component';
import {PokemonTypeColorPipe} from "./pokemons/pokemon-type-color.pipe";
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { CurrencyAppComponent} from './currency-exchange/currency-view/app.component';
import { HomeComponent } from './_home/home.component';
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {HttpClientModule} from "@angular/common/http";
import {BanqueAppComponent} from "./banque/banque-view/banque-view.component";
import { NewAccountComponent } from './banque/new-account/new-account.component';
import { TransferComponent } from './banque/transfer/transfer.component';

@NgModule({
  declarations: [
    AppComponent,
    PokemonDetailsComponent,
    BorderCardDirective,
    PokemonsViewComponent,
    PokemonTypeColorPipe,
    CurrencyAppComponent,
    HomeComponent,
    BanqueAppComponent,
    NewAccountComponent,
    TransferComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
