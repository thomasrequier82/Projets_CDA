import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConversionDeviseComponent } from './conversion-devise.component';

describe('ConversionDeviseComponent', () => {
  let component: ConversionDeviseComponent;
  let fixture: ComponentFixture<ConversionDeviseComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ConversionDeviseComponent ]
    })
      .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ConversionDeviseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
