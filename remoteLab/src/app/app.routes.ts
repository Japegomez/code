import { Routes } from '@angular/router';
import { LaboratoryComponent } from './components/laboratory/laboratory.component';
import { UnauthorizedComponent } from './components/unauthorized/unauthorized.component';

export const routes: Routes = [ 
    {path: '', component: LaboratoryComponent},
    {path: 'unauthorized', component: UnauthorizedComponent}, { path: '**', redirectTo: 'unauthorized' }];
