import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EnSerieComponent } from './en-serie.component';

describe('EnSerieComponent', () => {
  let component: EnSerieComponent;
  let fixture: ComponentFixture<EnSerieComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EnSerieComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(EnSerieComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
