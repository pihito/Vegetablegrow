import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CapteurOverviewComponent } from './capteur-overview.component';

describe('CapteurOverviewComponent', () => {
  let component: CapteurOverviewComponent;
  let fixture: ComponentFixture<CapteurOverviewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CapteurOverviewComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CapteurOverviewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
