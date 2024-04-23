import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EnParaleloComponent } from './en-paralelo.component';

describe('EnParaleloComponent', () => {
  let component: EnParaleloComponent;
  let fixture: ComponentFixture<EnParaleloComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EnParaleloComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(EnParaleloComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
