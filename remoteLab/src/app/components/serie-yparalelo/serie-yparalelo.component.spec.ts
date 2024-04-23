import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SerieYParaleloComponent } from './serie-yparalelo.component';

describe('SerieYParaleloComponent', () => {
  let component: SerieYParaleloComponent;
  let fixture: ComponentFixture<SerieYParaleloComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SerieYParaleloComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(SerieYParaleloComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
