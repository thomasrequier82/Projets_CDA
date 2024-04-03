import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {POKEMONS} from "../mock-pokemons";

@Component({
  selector: 'banque-view-pokemon-details',
  templateUrl: './pokemon-details.component.html',
  styleUrls: ['./pokemon-details.component.css']
})
export class PokemonDetailsComponent implements OnInit {

  id!: number;
  hp!: number;
  cp!: number;
  name!: string;
  picture!: string;
  types!: Array<string>;
  created!: Date;

  constructor(private route: ActivatedRoute) {
  }

  ngOnInit(){
    this.id = Number(this.route.snapshot.params["id"]) - 1;
    this.name = POKEMONS[this.id].name;
    this.hp = POKEMONS[this.id].hp;
    this.cp = POKEMONS[this.id].cp;
    this.picture = POKEMONS[this.id].picture;
    this.types = POKEMONS[this.id].types;
    this.created = POKEMONS[this.id].created;
  }

  getPokemon(){
    return POKEMONS[this.id];
  }
}
