import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {Router} from "@angular/router";
import {ACCOUNTS} from "../mock-accounts";

@Component({
  selector: 'app-new-account',
  templateUrl: './new-account.component.html',
  styleUrls: ['./new-account.component.css']
})
export class NewAccountComponent implements OnInit {

  public newAccountForm!: FormGroup;

  constructor(private formBuilder: FormBuilder,
              private router: Router) { }

  ngOnInit() {
    this.newAccountForm = this.formBuilder.group({
        'accountName': ['', Validators.required],
        'accountOwnerFirstname': ['', Validators.required],
        'accountOwnerLastname': ['', Validators.required]
    });
    console.log(this.newAccountForm);
  }

  onSubmit() {
    ACCOUNTS.push(
      {
        id: ACCOUNTS.length + 1,
        name: this.newAccountForm.value['accountName'],
        owner: [this.newAccountForm.value['accountOwnerFirstname'],
                this.newAccountForm.value['accountOwnerLastname']],
        money: 0
      }
    )
    this.router.navigate(['/banque']).then();
  }
}
