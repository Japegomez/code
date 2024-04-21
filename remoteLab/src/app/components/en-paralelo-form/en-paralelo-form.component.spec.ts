import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EnParaleloFormComponent } from './en-paralelo-form.component';

describe('EnParaleloFormComponent', () => {
  let component: EnParaleloFormComponent;
  let fixture: ComponentFixture<EnParaleloFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EnParaleloFormComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(EnParaleloFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
