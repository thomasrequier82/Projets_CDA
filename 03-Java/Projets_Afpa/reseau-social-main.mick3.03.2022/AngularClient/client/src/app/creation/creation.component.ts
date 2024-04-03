import {Component} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Md5} from "ts-md5/dist/md5";
import {FormBuilder, FormGroup, Validators} from "@angular/forms";

@Component({
  selector: 'app-creation',
  templateUrl: './creation.component.html'
})
export class CreationComponent {
  nom!: string;
  prenom!: string;
  mail!: string;
  password!: string;
  date!: Date;
  photo!: string;
  phone!: string;
  newAccountForm!: FormGroup;

  constructor(private http: HttpClient,
              private md5: Md5,
              private formBuilder: FormBuilder) { }

  ngOnInit() {
    this.newAccountForm = this.formBuilder.group({
      'nom': ['', Validators.required],
      'prenom': ['', Validators.required],
      'mail': ['', [Validators.required, Validators.pattern("^[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,4}$")]],
      'password': ['', Validators.required],
      'dateNaissance': [''],
      'photo': [''],
      'phone': ['']
    });
  }

  onSubmit() {

    // TODO : http post java <=> sql
    /*
      INSERT INTO passwords(hash, type) VALUES ("","MD5");
      INSERT INTO infos_personnelles(email, nom, prenom, date_de_naissance, telephone, photo) VALUES ("","","","","","")
      INSERT INTO utilisateurs(password, login) VALUES ((SELECT id FROM passwords WHERE hash = ""),
      (SELECT email FROM infos_personnelles WHERE email = ""));
     */
    this.password = this.newAccountForm.value['password'];
    console.log("test");
    const password = this.password;
    console.log(password);
    console.log(this.md5.appendStr(password).end());
    const passHashed = this.md5.appendStr(this.password).end();
    console.log(passHashed);

    // REQUETE SQL
    //594f803b380a41396ed63dca39503542



    /*ACCOUNTS.push(
      {
        id: ACCOUNTS.length + 1,
        name: this.newAccountForm.value['accountName'],
        owner: [this.newAccountForm.value['accountOwnerFirstname'],
          this.newAccountForm.value['accountOwnerLastname']],
        money: 0
      }
    )
    this.router.navigate(['/banque']).then();*/

  }

}
