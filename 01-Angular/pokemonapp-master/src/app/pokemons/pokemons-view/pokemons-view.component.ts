import { Component, OnInit } from '@angular/core';
import { Pokemon } from '../pokemon';
import { POKEMONS } from '../mock-pokemons';
import {Router} from "@angular/router";

@Component({
  selector: 'pokemons-view',
  templateUrl: './pokemons-view.component.html',
})
export class PokemonsViewComponent implements OnInit {
  private pokemons!: Array<Pokemon>;
  private title: string = "Pokémons";

  constructor(private router: Router) {
  }

  ngOnInit() {
    this.pokemons = POKEMONS;
  }

  getTitle(){
    return this.title;
  }

  getPokemons(){
    return this.pokemons;
  }

  onClick(pokemon: Pokemon) {
    this.router.navigate([`/pokemons/${pokemon.id}`]);
  }
}
