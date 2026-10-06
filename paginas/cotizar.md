# Documentación Completa y Código Autocontenido: Cotizador Unificado

> **Ruta URL:** `/cotizar`  
> **Archivo de Página:** `src/app/cotizar/page.tsx`  
> **Nota de Portabilidad:** Este documento incluye todo el código fuente de la página, sus componentes específicos, la estructura compartida del Layout (Header, Footer, Nav, CSS) y las constantes de negocio para permitir la generación de mockups HTML independientes sin depender del directorio `@src`.

---

## 1. Código Fuente de la Página (`src/app/cotizar/page.tsx`)

```tsx
import type { Metadata } from 'next';
import CotizadorHero from '@/components/cotizar/unified/CotizadorHero';
import CotizadorUnificado from '@/components/cotizar/unified/CotizadorUnificado';
import CotizadorRecargos from '@/components/cotizar/unified/CotizadorRecargos';
import {
  EXPRESS_PRICE_PER_KM,
  EXPRESS_TIERS,
  LOW_COST_PRICE_PER_KM,
  LOW_COST_TIERS,
} from '@/lib/pricing';
import {
  CONSULT_THRESHOLD_KM,
  EXPRESS_CUTOFF_TIME,
  EXPRESS_LEAD_TIME,
  LOWCOST_CUTOFF_TIME,
  LOWCOST_DELIVERY_DEADLINE,
  PERIPHERY_PRICE_PER_KM,
  STANDARD_BULLET_DIMENSIONS_CM,
  STANDARD_WEIGHT_KG,
} from '@/lib/promises';

const formatArs = (value: number) => `$${value.toLocaleString('es-AR')}`;

const baseUrl = 'https://www.enviosdosruedas.com';

export const dynamic = 'force-dynamic';

const TITLE = 'Cotizá tu Envío en Moto | Express y LowCost | Envíos DosRuedas';
const DESCRIPTION =
  'Cargá el retiro y la entrega una vez y compará la tarifa Express y LowCost para tu envío en Mar del Plata. Elegís el servicio y confirmás por WhatsApp.';

export const metadata: Metadata = {
  title: 'Cotizá tu Envío en Moto | Express y LowCost',
  description: DESCRIPTION,
  alternates: {
    canonical: `${baseUrl}/cotizar`,
  },
  openGraph: {
    title: TITLE,
    description: DESCRIPTION,
    url: `${baseUrl}/cotizar`,
    type: 'website',
    locale: 'es_AR',
  },
  twitter: {
    card: 'summary_large_image',
    title: TITLE,
    description: DESCRIPTION,
    images: [`${baseUrl}/og-image.jpg`],
    creator: '@enviosdosruedas',
  },
};

const jsonLdSchema = {
  '@context': 'https://schema.org',
  '@type': 'WebApplication',
  name: 'Cotizador de Envíos Envíos DosRuedas',
  applicationCategory: 'BusinessApplication',
  operatingSystem: 'All',
  url: `${baseUrl}/cotizar`,
  description:
    'Cotizador interactivo que calcula en una sola carga la tarifa Express y la tarifa LowCost de un envío en moto en Mar del Plata.',
  areaServed: [{ '@type': 'City', name: 'Mar del Plata' }],
  offers: [
    {
      '@type': 'Offer',
      name: 'Envío Express en moto',
      priceCurrency: 'ARS',
      price: String(EXPRESS_TIERS[0].price),
      description: `Tarifa por zona desde 0 a ${EXPRESS_TIERS[0].maxKm} km. Entrega en la franja horaria que elijas.`,
    },
    {
      '@type': 'Offer',
      name: 'Envío LowCost en moto',
      priceCurrency: 'ARS',
      price: String(LOW_COST_TIERS[0].price),
      description: `Tarifa por zona desde 0 a ${LOW_COST_TIERS[0].maxKm} km. Entrega programada el mismo día.`,
    },
  ],
  provider: {
    '@type': 'LocalBusiness',
    '@id': `${baseUrl}#localbusiness`,
    name: 'Envíos DosRuedas',
    telephone: '+54-223-660-2699',
    address: {
      '@type': 'PostalAddress',
      streetAddress: 'Friuli 1972',
      addressLocality: 'Mar del Plata',
      addressRegion: 'Buenos Aires',
      postalCode: '7600',
      addressCountry: 'AR',
    },
  },
};

/**
 * Filas de la tabla pública. Se derivan de `pricing.ts` para que el texto y el
 * cotizador nunca puedan contradecirse: nadie escribe un importe a mano acá.
 */
const TARIFAS = [
  ...EXPRESS_TIERS.map((tier, i) => ({
    rango: `${tier.minKm} a ${tier.maxKm} km`,
    express: formatArs(tier.price),
    lowcost: formatArs(LOW_COST_TIERS[i].price),
  })),
  {
    rango: `Más de ${EXPRESS_TIERS[EXPRESS_TIERS.length - 1].maxKm} km`,
    express: `${formatArs(EXPRESS_PRICE_PER_KM)} por km`,
    lowcost: `${formatArs(LOW_COST_PRICE_PER_KM)} por km`,
  },
];

export default function Page() {
  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLdSchema) }}
      />

      <div
        id="cotizar-page"
        className="w-full bg-brand-blue-500 text-white min-h-dvh relative overflow-hidden font-sans"
      >
        <CotizadorHero />

        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 lg:py-14 space-y-10 lg:space-y-14 relative z-10">
          <CotizadorUnificado />

          {/* Tabla de tarifas: el respaldo textual de lo que calcula el formulario. */}
          <section aria-labelledby="tabla-tarifas" className="space-y-5">
            <div className="space-y-2">
              <span className="inline-block px-3 py-1 rounded-full bg-brand-yellow-500/10 border border-brand-yellow-500/30 text-brand-yellow-500 font-subheading text-xs uppercase tracking-widest">
                Tarifas 2026
              </span>
              <h2
                id="tabla-tarifas"
                className="font-display text-2xl sm:text-3xl uppercase tracking-tight text-white"
              >
                Cuánto cuesta cada zona
              </h2>
              <p className="font-sans text-white/90 leading-relaxed max-w-3xl text-sm sm:text-base">
                Las dos columnas usan la misma distancia, medida sobre la calle y no ida y vuelta
                en línea recta. Express se entrega en la franja de 3 hs que elijas; LowCost, en el
                día y sin elección de horario, antes de las {LOWCOST_DELIVERY_DEADLINE}.
              </p>
            </div>

            <div className="overflow-x-auto rounded-2xl border border-white/15 bg-white/5 backdrop-blur-md">
              <table className="w-full min-w-136 text-left border-collapse">
                <caption className="sr-only">
                  Tarifas por zona de distancia para los servicios Express y LowCost
                </caption>
                <thead>
                  <tr className="border-b border-white/15">
                    <th scope="col" className="px-4 sm:px-5 py-3 font-subheading text-xs uppercase tracking-widest text-white/85">
                      Zona
                    </th>
                    <th scope="col" className="px-4 sm:px-5 py-3 font-subheading text-xs uppercase tracking-widest text-brand-yellow-500">
                      Express
                    </th>
                    <th scope="col" className="px-4 sm:px-5 py-3 font-subheading text-xs uppercase tracking-widest text-white">
                      LowCost
                    </th>
                  </tr>
                </thead>
                <tbody>
                  {TARIFAS.map((fila, i) => (
                    <tr
                      key={fila.rango}
                      className={i % 2 === 1 ? 'bg-white/4' : undefined}
                    >
                      <th
                        scope="row"
                        className="px-4 sm:px-5 py-3 font-mono text-sm text-white/90 font-normal tabular-nums"
                      >
                        {fila.rango}
                      </th>
                      <td className="px-4 sm:px-5 py-3 font-mono text-sm font-bold text-brand-yellow-500 tabular-nums">
                        {fila.express}
                      </td>
                      <td className="px-4 sm:px-5 py-3 font-mono text-sm font-bold text-white tabular-nums">
                        {fila.lowcost}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            <dl className="grid gap-x-8 gap-y-4 sm:grid-cols-3">
              <div>
                <dt className="font-subheading text-xs uppercase tracking-widest text-brand-yellow-500">
                  Cobertura
                </dt>
                <dd className="font-sans text-sm text-white/85 leading-relaxed mt-1">
                  Todo Mar del Plata. Hasta {CONSULT_THRESHOLD_KM} km el cálculo es automático; más
                  allá, la tarifa se conversa con el equipo.
                </dd>
              </div>
              <div>
                <dt className="font-subheading text-xs uppercase tracking-widest text-brand-yellow-500">
                  Peso y medidas
                </dt>
                <dd className="font-sans text-sm text-white/85 leading-relaxed mt-1">
                  Hasta {STANDARD_WEIGHT_KG} kg o {STANDARD_BULLET_DIMENSIONS_CM} por bulto sin
                  recargo. Más que eso suma un recargo por bulto extra, que se calcula según el
                  servicio.
                </dd>
              </div>
              <div>
                <dt className="font-subheading text-xs uppercase tracking-widest text-brand-yellow-500">
                  Cortes
                </dt>
                <dd className="font-sans text-sm text-white/85 leading-relaxed mt-1">
                  Express: con {EXPRESS_LEAD_TIME}, hasta las {EXPRESS_CUTOFF_TIME}. LowCost:
                  pedidos antes de las {LOWCOST_CUTOFF_TIME}, entrega antes de las{' '}
                  {LOWCOST_DELIVERY_DEADLINE}.
                </dd>
              </div>
            </dl>
          </section>

          <CotizadorRecargos />

          <section aria-labelledby="cobertura-guia" className="space-y-4">
            <h2
              id="cobertura-guia"
              className="font-display text-2xl sm:text-3xl uppercase tracking-tight text-white"
            >
              Dónde llegamos
            </h2>
            <p className="font-sans text-white/90 leading-relaxed max-w-3xl text-sm sm:text-base">
              Llegamos a todo Mar del Plata: Centro, Güemes, Chauvín, Los Troncos, Puerto, Playa
              Grande, Punta Mogotes, Constitución y Camet, entre otros barrios. Más allá de los 10
              km de ruta cotizamos por kilómetro, y el cálculo automático llega hasta los{' '}
              {CONSULT_THRESHOLD_KM} km. Los destinos fuera de la ciudad, como Batán o Sierra de los
              Padres, van a {formatArs(PERIPHERY_PRICE_PER_KM)} por km de ruta y los vemos por
              WhatsApp.
            </p>
          </section>
        </div>
      </div>
    </>
  );
}

```

---

## 2. Componentes Específicos Importados por esta Página

### Componente: `src/components/cotizar/unified/CotizadorHero.tsx`

```tsx
'use client';

import React from 'react';
import { motion, useReducedMotion } from 'motion/react';
import { GitCompareArrows, MapPin, MessageCircle } from 'lucide-react';
import HeroProceduralBackground from '@/components/ui/HeroProceduralBackground';
import CTANestedPill from '@/components/ui/CTANestedPill';
import Badge from '@/components/ui/Badge';

/**
 * Hero de la guía, no de un servicio. No vende Express ni LowCost: explica que
 * cargás un envío una vez y recibís las dos tarifas. La promesa es la del flujo.
 */
export default function CotizadorHero() {
  const reduceMotion = useReducedMotion();

  return (
    <section
      id="cotizador-hero"
      className="relative w-full overflow-hidden bg-brand-blue-700 text-white min-h-auto lg:min-h-[52vh] flex items-center pt-20 pb-8 sm:pt-24 lg:pt-28 lg:pb-12 border-b border-white/10"
    >
      <HeroProceduralBackground variant="express" />

      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-12 items-center">
          <motion.div
            initial={reduceMotion ? undefined : { opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
            className="lg:col-span-7 space-y-6 text-center lg:text-left"
          >
            <Badge
              variant="accent"
              size="lg"
              className="-rotate-1"
              icon={<GitCompareArrows className="h-4 w-4" />}
            >
              Dos servicios · Una sola carga
            </Badge>

            <h1 className="text-5xl sm:text-6xl lg:text-[4.75rem] xl:text-[5.25rem] font-display uppercase tracking-tight leading-[0.92] text-white">
              <span>COTIZÁ TU </span>
              <span className="inline-block bg-brand-yellow-500 text-brand-blue-900 px-3 py-1 rounded-lg transform -rotate-1 shadow-glow-yellow mx-1">
                ENVÍO
              </span>
              <span className="block">Y COMPARÁ</span>
            </h1>

            <p className="text-base sm:text-lg font-sans text-white/90 max-w-2xl mx-auto lg:mx-0 leading-relaxed font-light">
              Cargá el retiro y la entrega una sola vez. Te mostramos la tarifa Express y la
              LowCost para esa distancia exacta, y vos elegís cuál querés. Sin registro, sin
              llamadas, sin letra chica.
            </p>

            <div className="flex justify-center lg:justify-start pt-2">
              <CTANestedPill
                href="#cotizador-form"
                variant="primary"
                size="large"
                className="w-full sm:w-auto"
              >
                Cargar mi envío
              </CTANestedPill>
            </div>
          </motion.div>

          {/* El flujo en tres líneas: es la guía completa de la página, en miniatura. */}
          <motion.div
            initial={reduceMotion ? undefined : { opacity: 0, scale: 0.97 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.6, delay: 0.15, ease: [0.16, 1, 0.3, 1] }}
            className="lg:col-span-5 w-full max-w-lg mx-auto"
          >
            <div className="p-2.5 rounded-2xl bg-brand-blue-50/20 border border-brand-blue-100/40 shadow-2xl backdrop-blur-md">
              <div className="bg-brand-blue-700 rounded-xl border border-white/20 overflow-hidden divide-y divide-white/10">
                {[
                  { n: '01', icon: MapPin, t: 'Cargás retiro y entrega', s: 'Medimos la distancia real por calle' },
                  { n: '02', icon: GitCompareArrows, t: 'Ves las dos tarifas', s: 'Express y LowCost sobre la misma escala' },
                  { n: '03', icon: MessageCircle, t: 'Elegís y confirmás', s: 'Te llevamos el pedido por WhatsApp' },
                ].map((paso) => (
                  <div key={paso.n} className="flex items-center gap-4 p-4 sm:p-5">
                    <span className="font-mono text-xs text-brand-yellow-500 tabular-nums shrink-0">
                      {paso.n}
                    </span>
                    <paso.icon className="h-4 w-4 text-white/60 shrink-0" aria-hidden="true" />
                    <span className="min-w-0">
                      <span className="block font-subheading text-sm uppercase tracking-wider text-white">
                        {paso.t}
                      </span>
                      <span className="block font-sans text-xs text-white/85 mt-0.5">{paso.s}</span>
                    </span>
                  </div>
                ))}
              </div>
            </div>
          </motion.div>
        </div>
      </div>
    </section>
  );
}

```

### Componente: `src/components/ui/HeroProceduralBackground.tsx`

```tsx
import React from 'react';

export interface HeroProceduralBackgroundProps {
  variant?: 'express' | 'lowcost' | 'flex' | '3pl' | 'community' | 'contact' | 'default';
  /**
   * Eje tonal del fondo. `blue` (por defecto) es el azul de marca #0950F6 con
   * grilla punteada blanca; `yellow` es el amarillo vial #FFEC01 SIN gradiente,
   * con grilla azul punteada al 5% y un halo blanco suave encima.
   * En ambos tonos nada puede ser más oscuro que #0950F6.
   */
  tone?: 'blue' | 'yellow';
  className?: string;
}

/**
 * Fondo procedural de hero. Server Component: el gate de `prefers-reduced-motion`
 * es CSS (`motion-safe:`), no `useReducedMotion()`, para no romper el hydration —
 * `useReducedMotion()` devuelve `false` en el servidor y el valor real en el cliente.
 * 
 * Gradiente canónico Max (Ajuste #0950F6): linear-gradient(135deg, #0950F6 0%, #0950F6 55%, #3570F8 100%)
 * Halos con rgba(9,80,246,α) y rgba(255,236,1,α) — NUNCA rgba(6,54,165,…) ni rgba(0,39,124,…)
 */
export default function HeroProceduralBackground({
  variant = 'default',
  tone = 'blue',
  className = '',
}: HeroProceduralBackgroundProps) {
  const isYellow = tone === 'yellow';
  const accent = isYellow ? 'var(--color-brand-blue-500)' : 'var(--color-brand-yellow-500)';
  const softAccent = isYellow ? 'var(--color-brand-blue-500)' : 'var(--color-brand-blue-300)';
  const white = isYellow ? 'var(--color-brand-blue-500)' : 'var(--color-white)';
  const gridOpacity = isYellow ? 0.05 : 0.07;
  const artOpacity = isYellow ? 0.14 : 0.2;

  // Gradiente canónico Max: #0950F6 → #0950F6 → #3570F8 (nada más oscuro que #0950F6)
  const canonicalGradient = 'linear-gradient(135deg, #0950F6 0%, #0950F6 55%, #3570F8 100%)';

  return (
    <div
      className={`absolute inset-0 pointer-events-none select-none overflow-hidden ${className}`}
    >
      {isYellow ? (
        <>
          {/* Tono amarillo: base plana, sin gradiente. */}
          <div className="absolute inset-0 bg-brand-yellow-500" />
          <div
            className="absolute inset-x-0 top-0 h-[70%]"
            style={{
              background:
                'radial-gradient(ellipse at 50% 0%, rgba(255,255,255,0.55) 0%, rgba(255,255,255,0) 70%)',
            }}
          />
        </>
      ) : (
        <>
          {/* 1. Gradiente base canónico Max (Ajuste #0950F6) */}
          <div
            className="absolute inset-0"
            style={{ background: canonicalGradient }}
          />

          {/* 2. Procedural Dynamic Radial Highlights (CSS Glows) — Todos teñidos con brand colors */}
          <div
            className="absolute -top-32 -left-32 w-125 h-125 rounded-full pointer-events-none"
            style={{
              background:
                'radial-gradient(circle, rgba(9,80,246,0.35) 0%, rgba(9,80,246,0.18) 50%, transparent 70%)',
              filter: 'blur(80px)',
            }}
          />

          <div
            className="absolute top-1/4 -right-32 w-150 h-150 rounded-full pointer-events-none"
            style={{
              background:
                variant === 'express' || variant === 'lowcost'
                  ? 'radial-gradient(circle, rgba(255,236,1,0.22) 0%, rgba(255,236,1,0.06) 45%, transparent 70%)'
                  : 'radial-gradient(circle, rgba(255,236,1,0.16) 0%, rgba(9,80,246,0.12) 50%, transparent 70%)',
              filter: 'blur(90px)',
            }}
          />

          <div
            className="absolute -bottom-40 left-1/3 w-137.5 h-137.5 rounded-full pointer-events-none"
            style={{
              background: 'radial-gradient(circle, rgba(9,80,246,0.4) 0%, transparent 70%)',
              filter: 'blur(100px)',
            }}
          />
        </>
      )}

      {/* 3. Mathematical Vector Grid Topology (Pure SVG, 0 KB image) */}
      <svg
        className="absolute inset-0 w-full h-full"
        style={{ opacity: gridOpacity }}
        xmlns="http://www.w3.org/2000/svg"
      >
        <defs>
          <pattern
            id={`hero-procedural-grid-${tone}`}
            width="48"
            height="48"
            patternUnits="userSpaceOnUse"
          >
            <path
              d="M 48 0 L 0 0 0 48"
              fill="none"
              stroke={white}
              strokeWidth="0.75"
              strokeDasharray="2,6"
            />
            <circle cx="0" cy="0" r="1.5" fill={accent} />
          </pattern>
        </defs>
        <rect width="100%" height="100%" fill={`url(#hero-procedural-grid-${tone})`} />
      </svg>

      {/* 4. Variant-Specific Procedural Vector Graphics */}
      {variant === 'express' && (
        <svg
          className="absolute inset-0 w-full h-full"
          style={{ opacity: artOpacity }}
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 1440 600"
          preserveAspectRatio="none"
        >
          {/* Animated Speed & Logistics Arteries */}
          <path
            d="M -100 450 Q 400 200 900 380 T 1600 150"
            fill="none"
            stroke={accent}
            strokeWidth="2.5"
            strokeDasharray="12 16"
            className="motion-safe:animate-pulse"
          />
          <path
            d="M -100 300 Q 500 480 1000 250 T 1600 350"
            fill="none"
            stroke={softAccent}
            strokeWidth="1.5"
            strokeDasharray="8 12"
          />
          <circle cx="450" cy="240" r="4" fill={accent} />
          <circle cx="950" cy="360" r="5" fill={accent} />
        </svg>
      )}

      {variant === 'lowcost' && (
        <svg
          className="absolute inset-0 w-full h-full"
          style={{ opacity: artOpacity }}
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 1440 600"
          preserveAspectRatio="none"
        >
          {/* Concentric Cluster Routing Rings */}
          <circle cx="1100" cy="300" r="160" fill="none" stroke={accent} strokeWidth="1" strokeDasharray="4 8" />
          <circle cx="1100" cy="300" r="280" fill="none" stroke={softAccent} strokeWidth="1" strokeDasharray="6 12" />
          <circle cx="1100" cy="300" r="400" fill="none" stroke={white} strokeWidth="0.75" strokeDasharray="4 16" />
          <line x1="200" y1="300" x2="1100" y2="300" stroke={accent} strokeWidth="1.5" strokeDasharray="8 8" />
        </svg>
      )}

      {variant === 'flex' && (
        <svg
          className="absolute inset-0 w-full h-full"
          style={{ opacity: artOpacity }}
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 1440 600"
          preserveAspectRatio="none"
        >
          {/* Verified Dispatch Corridor Matrix */}
          <line x1="0" y1="180" x2="1440" y2="180" stroke={accent} strokeWidth="1.5" strokeDasharray="6 12" />
          <line x1="0" y1="420" x2="1440" y2="420" stroke={softAccent} strokeWidth="1" strokeDasharray="4 10" />
          <rect x="750" y="140" width="80" height="80" rx="16" fill="none" stroke={accent} strokeWidth="1.5" strokeDasharray="4 4" />
          <rect x="950" y="240" width="120" height="120" rx="24" fill="none" stroke={white} strokeWidth="1" strokeDasharray="6 8" />
        </svg>
      )}

      {variant === '3pl' && (
        <svg
          className="absolute inset-0 w-full h-full"
          style={{ opacity: artOpacity }}
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 1440 600"
          preserveAspectRatio="none"
        >
          {/* Inventory Hub Node Matrix */}
          <polygon points="900,150 1100,220 1000,420 800,350" fill="none" stroke={accent} strokeWidth="1.5" strokeDasharray="6 8" />
          <circle cx="900" cy="150" r="5" fill={accent} />
          <circle cx="1100" cy="220" r="5" fill={accent} />
          <circle cx="1000" cy="420" r="5" fill={accent} />
          <circle cx="800" cy="350" r="5" fill={accent} />
        </svg>
      )}

      {variant === 'community' && (
        <svg
          className="absolute inset-0 w-full h-full"
          style={{ opacity: artOpacity }}
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 1440 600"
          preserveAspectRatio="none"
        >
          {/* Social Network Node Links */}
          <line x1="300" y1="200" x2="700" y2="150" stroke={softAccent} strokeWidth="1" />
          <line x1="700" y1="150" x2="1100" y2="280" stroke={accent} strokeWidth="1.5" />
          <line x1="1100" y1="280" x2="900" y2="480" stroke={softAccent} strokeWidth="1" />
          <line x1="900" y1="480" x2="500" y2="400" stroke={accent} strokeWidth="1" />
          <line x1="500" y1="400" x2="300" y2="200" stroke={softAccent} strokeWidth="1" />
        </svg>
      )}

      {variant === 'contact' && (
        <svg
          className="absolute inset-0 w-full h-full"
          style={{ opacity: artOpacity }}
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 1440 600"
          preserveAspectRatio="none"
        >
          {/* GPS Coordinate Beacon Radar */}
          <circle
            cx="1050"
            cy="320"
            r="80"
            fill="none"
            stroke={accent}
            strokeWidth="1.5"
            className="motion-safe:animate-ping [animation-duration:4s]"
          />
          <circle cx="1050" cy="320" r="180" fill="none" stroke={accent} strokeWidth="1" strokeDasharray="4 8" />
          <circle cx="1050" cy="320" r="300" fill="none" stroke={softAccent} strokeWidth="0.75" strokeDasharray="6 12" />
          <circle cx="1050" cy="320" r="6" fill={accent} />
        </svg>
      )}
    </div>
  );
}

```

### Componente: `src/components/ui/CTANestedPill.tsx`

```tsx
'use client';

import React from 'react';
import Link from 'next/link';
import { ArrowRight } from 'lucide-react';
import { cn } from '@/lib/utils';
import { trackAnalytics } from '@/lib/analytics';

export type CTANestedPillVariant = 'primary' | 'blue' | 'elevated' | 'outline' | 'ghost';
export type CTANestedPillSize = 'compact' | 'default' | 'large' | 'lg';

export interface CTANestedPillProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  children: React.ReactNode;
  href?: string;
  variant?: CTANestedPillVariant;
  size?: CTANestedPillSize;
  icon?: React.ReactNode;
  iconPosition?: 'left' | 'right';
  className?: string;
  iconClassName?: string;
  target?: string;
  rel?: string;
}

/**
 * CTANestedPill Component
 * Standardized nested pill CTA interactive element (Button or Link).
 * Follows DESIGN.md specifications:
 * - Rounded-full, font-subheading, uppercase, tracking-wider, font-bold
 * - Embedded circular icon chip (w-8 h-8) with smooth hover translation
 * - Variants: --primary (yellow), --blue (para fondos amarillos), --elevated (white), --outline, --ghost
 */
export const CTANestedPill = React.forwardRef<HTMLButtonElement | HTMLAnchorElement, CTANestedPillProps>(
  (
    {
      children,
      href,
      variant = 'primary',
      size = 'default',
      icon,
      iconPosition = 'right',
      className,
      iconClassName,
      target,
      rel,
      disabled,
      ...buttonProps
    },
    ref
  ) => {
    const baseStyles =
      'cta-nested-pill group inline-flex items-center justify-between gap-3 rounded-full font-subheading uppercase tracking-wider font-bold transition-all duration-200 cursor-pointer focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-blue-500 focus-visible:ring-offset-2 select-none border';

    const normalizedSize = size === 'lg' ? 'large' : size;

    const sizeStyles = {
      compact: 'px-4 py-1.5 text-xs min-h-9',
      default: 'px-5 py-2 text-sm min-h-11',
      large: 'px-8 py-3 text-base min-h-13',
    }[normalizedSize];

    const variantStyles = {
      primary:
        'bg-brand-yellow-500 text-brand-blue-500 border-brand-yellow-500 shadow-accent-sm hover:shadow-cta-glow hover:bg-brand-yellow-400 active:scale-98 active:translate-y-px',
      // Para fondos amarillos (#FFEC01): azul de marca, texto blanco, chip amarillo.
      blue: 'bg-brand-blue-500 text-white border-brand-blue-500 shadow-[0_0_24px_rgba(9,80,246,0.28)] hover:bg-brand-blue-500 hover:border-brand-blue-500 active:scale-98 active:translate-y-px',
      elevated:
        'bg-white text-brand-blue-500 border-brand-blue-100 shadow-elevated hover:shadow-hover-lift hover:border-brand-blue-300 hover:text-brand-blue-500 active:scale-98',
      outline:
        'bg-transparent text-brand-blue-500 border-2 border-brand-blue-500 hover:bg-brand-blue-50 active:scale-98',
      ghost:
        'bg-transparent text-brand-blue-500 border-transparent hover:bg-brand-blue-50 active:scale-98',
    }[variant];

    const iconChipBase =
      'cta-nested-icon w-8 h-8 rounded-full flex items-center justify-center shrink-0 transition-all duration-200';

    const iconChipVariantStyles = {
      primary:
        'bg-transparent text-brand-blue-500 group-hover:bg-brand-blue-500 group-hover:text-brand-yellow-500 group-hover:translate-x-1',
      blue: 'bg-brand-yellow-500 text-brand-blue-500 group-hover:bg-brand-yellow-400 group-hover:translate-x-1',
      elevated:
        'bg-transparent text-brand-blue-500 group-hover:bg-brand-blue-500 group-hover:text-white group-hover:translate-x-1',
      outline:
        'bg-transparent text-brand-blue-500 group-hover:bg-brand-blue-500 group-hover:text-white group-hover:translate-x-1',
      ghost:
        'bg-transparent text-brand-blue-500 group-hover:bg-brand-blue-500 group-hover:text-white group-hover:translate-x-1',
    }[variant];

    const defaultIcon = <ArrowRight className="w-4 h-4" />;
    const renderedIcon = icon !== undefined ? icon : defaultIcon;

    const disabledStyles = disabled ? 'opacity-50 cursor-not-allowed pointer-events-none' : '';

    const combinedClassName = cn(
      baseStyles,
      sizeStyles,
      variantStyles,
      disabledStyles,
      className
    );

    const iconContent = (
      <span className={cn(iconChipBase, iconChipVariantStyles, iconClassName)}>
        {renderedIcon}
      </span>
    );

    const content = (
      <>
        {iconPosition === 'left' && iconContent}
        <span className="truncate">{children}</span>
        {iconPosition === 'right' && iconContent}
      </>
    );

    const handleClick = (e: React.MouseEvent<HTMLAnchorElement | HTMLButtonElement>) => {
      if (href && (href.includes('wa.me') || href.includes('whatsapp.com'))) {
        trackAnalytics.whatsappClick('cta_pill', typeof children === 'string' ? children : undefined);
      } else if (buttonProps.id || typeof children === 'string') {
        trackAnalytics.ctaClick(buttonProps.id || 'cta_pill', typeof children === 'string' ? children : 'cta');
      }
      if (buttonProps.onClick) {
        buttonProps.onClick(e as React.MouseEvent<HTMLButtonElement>);
      }
    };

    if (href && !disabled) {
      return (
        <Link
          href={href}
          ref={ref as React.Ref<HTMLAnchorElement>}
          className={combinedClassName}
          target={target}
          rel={rel}
          onClick={handleClick}
        >
          {content}
        </Link>
      );
    }

    return (
      <button
        ref={ref as React.Ref<HTMLButtonElement>}
        type={buttonProps.type || 'button'}
        disabled={disabled}
        className={combinedClassName}
        {...buttonProps}
        onClick={handleClick}
      >
        {content}
      </button>
    );
  }
);

CTANestedPill.displayName = 'CTANestedPill';

export default CTANestedPill;

```

### Componente: `src/components/ui/Badge.tsx`

```tsx
'use client';

import React from 'react';
import { cn } from '@/lib/utils';

export type BadgeVariant =
  | 'urgent'
  | 'secure'
  | 'economic'
  | 'flex'
  | 'neutral'
  | 'outline'
  | 'primary'
  | 'accent';

export type BadgeSize = 'sm' | 'md' | 'lg';

export interface BadgeProps extends React.HTMLAttributes<HTMLSpanElement> {
  children: React.ReactNode;
  variant?: BadgeVariant;
  size?: BadgeSize;
  icon?: React.ReactNode;
  rounded?: 'full' | 'lg' | 'md';
  className?: string;
}

/**
 * Badge Component
 * Official badge pill system for statuses, trust indicators, and service types.
 * Follows DESIGN.md specifications:
 * - font-subheading, text-label, uppercase, tracking-wider, font-bold
 * - rounded-full or rounded-lg, padding var(--space-1) var(--space-2), border
 */
export const Badge: React.FC<BadgeProps> = ({
  children,
  variant = 'neutral',
  size = 'md',
  icon,
  rounded = 'full',
  className,
  ...props
}) => {
  const baseStyles =
    'inline-flex items-center gap-1.5 font-subheading uppercase tracking-wider font-bold border transition-colors select-none';

  const roundedStyles = {
    full: 'rounded-full',
    lg: 'rounded-lg',
    md: 'rounded-md',
  }[rounded];

  const sizeStyles = {
    sm: 'px-2 py-0.5 text-2xs leading-tight',
    md: 'px-3 py-1 text-xs leading-tight',
    lg: 'px-4 py-1.5 text-sm leading-tight',
  }[size];

  const variantStyles = {
    urgent:
      'bg-brand-yellow-500 text-brand-blue-500 border-brand-yellow-400 shadow-accent-sm',
    secure: 'bg-brand-blue-50 text-brand-blue-500 border-brand-blue-200',
    economic: 'bg-brand-blue-50 text-brand-blue-500 border-brand-blue-200',
    flex: 'bg-brand-yellow-100 text-brand-blue-500 border-brand-yellow-200',
    neutral: 'bg-white text-brand-blue-500 border-brand-blue-100 shadow-sm',
    outline: 'bg-transparent text-brand-blue-500 border-brand-blue-500',
    primary: 'bg-brand-blue-500 text-white border-brand-blue-500',
    accent:
      'bg-brand-yellow-500 text-brand-blue-500 border-brand-yellow-500 shadow-accent-sm',
  }[variant];

  return (
    <span
      className={cn(baseStyles, roundedStyles, sizeStyles, variantStyles, className)}
      {...props}
    >
      {icon && <span className="shrink-0">{icon}</span>}
      <span>{children}</span>
    </span>
  );
};

export default Badge;

```

### Componente: `src/components/cotizar/unified/CotizadorUnificado.tsx`

```tsx
'use client';

import React from 'react';
import { Calculator } from 'lucide-react';
import CotizadorForm from './CotizadorForm';
import CotizadorComparativa from './CotizadorComparativa';
import CotizadorMapa from './CotizadorMapa';
import CotizadorGuia from './CotizadorGuia';
import Badge from '@/components/ui/Badge';
import { useCotizadorUnificado } from '@/hooks/cotizador/useCotizadorUnified';

/**
 * Isla única del cotizador. Todo el estado vive acá: el formulario y la
 * comparación se mueven juntos.
 *
 * No hay cotización por lotes: LowCost es un reparto programado en el día, no un
 * precio por agrupar envíos de un mismo cliente (decisión del dueño 2026-09-29).
 */
export default function CotizadorUnificado() {
  const form = useCotizadorUnificado();

  return (
    <div className="space-y-8 lg:space-y-10">
      <CotizadorGuia />

      <section
        id="cotizador-form"
        aria-label="Cotizador de envíos"
        className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-stretch scroll-mt-20"
      >
        <article className="lg:col-span-7 flex flex-col rounded-3xl bg-white/10 backdrop-blur-md border border-white/20 p-2.5 shadow-xl">
          <div className="bg-brand-blue-700 p-6 sm:p-8 rounded-2xl border border-white/10 flex flex-col h-full text-white relative overflow-hidden">
            <Calculator
              className="absolute -bottom-10 -right-10 w-64 h-64 text-white/4 pointer-events-none"
              aria-hidden="true"
            />

            <header className="relative z-10 mb-6">
              <Badge
                variant="outline"
                size="sm"
                className="border-brand-yellow-500/40 text-brand-yellow-500 -rotate-1"
              >
                Mar del Plata · Sin registro
              </Badge>
              <h2 className="text-2xl sm:text-3xl font-display uppercase tracking-tight text-white mt-3">
                Contanos del envío
              </h2>
              <p className="text-white/90 text-sm font-sans mt-1 leading-relaxed">
                Con el origen y el destino alcanzamos el precio de los dos servicios.
              </p>
            </header>

            <CotizadorForm form={form} />

            <CotizadorComparativa form={form} error={form.error} />
          </div>
        </article>

        <CotizadorMapa form={form} />
      </section>

    </div>
  );
}

```

### Componente: `src/components/cotizar/unified/CotizadorForm.tsx`

```tsx
'use client';

import React from 'react';
import { MapPin, User, Phone, Package } from 'lucide-react';
import AddressAutocomplete from '@/components/ui/AddressAutocomplete';
import CTANestedPill from '@/components/ui/CTANestedPill';
import InputField from '@/components/ui/InputField';
import type { UseCotizadorUnificadoReturn } from '@/hooks/cotizador/useCotizadorUnified';

interface CotizadorFormProps {
  form: UseCotizadorUnificadoReturn;
}

/**
 * Un solo formulario para los dos servicios. Los campos de servicio que antes
 * vivían en cada cotizador (franja horaria, tipo de producto por servicio) no
 * aparecen acá: la elección del servicio es el último paso, con el número a la vista.
 */
export default function CotizadorForm({ form }: CotizadorFormProps) {
  return (
    <form
      noValidate
      onSubmit={form.handleCalculate}
      onFocus={form.handleInputFocus}
      className="space-y-5 relative z-10"
    >
      <div className="space-y-1.5">
        <label
          htmlFor="guia-origen-input"
          className="text-xs font-subheading uppercase tracking-wider font-bold text-white flex items-center gap-1.5"
        >
          <MapPin className="h-3.5 w-3.5" />
          Dirección de Origen (Retiro)
        </label>
        <AddressAutocomplete
          id="guia-origen-input"
          placeholder="Ej: Av. Colón 1234, Mar del Plata"
          value={form.origen}
          onChange={form.setOrigen}
          onSelectCoordinate={form.setOrigenCoords}
          required
          className="w-full h-11 bg-white border-2 border-brand-blue-100 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-brand-blue-700 focus-visible:border-brand-blue-700 rounded-xl px-4 text-sm transition-all text-brand-blue-900 placeholder:text-brand-blue-500 font-sans shadow-sm"
        />
      </div>

      <div className="space-y-1.5">
        <label
          htmlFor="guia-destino-input"
          className="text-xs font-subheading uppercase tracking-wider font-bold text-white flex items-center gap-1.5"
        >
          <MapPin className="h-3.5 w-3.5" />
          Dirección de Destino (Entrega)
        </label>
        <AddressAutocomplete
          id="guia-destino-input"
          placeholder="Ej: Juan B. Justo 5678, Mar del Plata"
          value={form.destino}
          onChange={form.setDestino}
          onSelectCoordinate={form.setDestinoCoords}
          required
          className="w-full h-11 bg-white border-2 border-brand-blue-100 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-brand-blue-700 focus-visible:border-brand-blue-700 rounded-xl px-4 text-sm transition-all text-brand-blue-900 placeholder:text-brand-blue-500 font-sans shadow-sm"
        />
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
        <InputField
          id="guia-nombre-input"
          label="Nombre"
          placeholder="Tu nombre completo"
          value={form.nombre}
          onChange={(e) => form.setNombre(e.target.value)}
          required
          icon={<User className="h-3.5 w-3.5" />}
          labelClassName="text-white"
          containerClassName="space-y-1.5"
        />

        <InputField
          id="guia-telefono-input"
          label="Teléfono"
          placeholder="Tu teléfono de contacto"
          value={form.telefono}
          onChange={(e) => form.setTelefono(e.target.value)}
          required
          type="tel"
          icon={<Phone className="h-3.5 w-3.5" />}
          className="font-mono tabular-nums"
          labelClassName="text-white"
          containerClassName="space-y-1.5"
        />
      </div>

      <InputField
        id="guia-producto-input"
        label="Qué hay adentro"
        placeholder="Ej: Documentos, indumentaria, repuesto..."
        value={form.producto}
        onChange={(e) => form.setProducto(e.target.value)}
        required
        icon={<Package className="h-3.5 w-3.5" />}
        labelClassName="text-white"
        containerClassName="space-y-1.5"
      />

      <div className="pt-1">
        <CTANestedPill
          type="submit"
          variant="primary"
          size="large"
          disabled={form.isCalculating}
          className="w-full"
        >
          {form.isCalculating ? 'Midiendo la ruta...' : 'Ver las dos tarifas'}
        </CTANestedPill>
      </div>

      <p className="font-sans text-2xs text-white/60 text-center leading-snug">
        Las tarifas salen de nuestra tabla vigente. El pedido se confirma por WhatsApp.
      </p>
    </form>
  );
}

```

### Componente: `src/components/ui/AddressAutocomplete.tsx`

```tsx
'use client';

import React, { useState, useEffect, useRef } from 'react';
import { Search, MapPin, Loader2 } from 'lucide-react';

interface Suggestion {
  description: string;
  place_id: string;
}

interface AddressAutocompleteProps {
  id: string;
  placeholder: string;
  value: string;
  onChange: (value: string) => void;
  onSelectCoordinate: (coords: { lat: number; lng: number } | null) => void;
  required?: boolean;
  className?: string;
}

export default function AddressAutocomplete({
  id,
  placeholder,
  value,
  onChange,
  onSelectCoordinate,
  required = false,
  className = '',
}: AddressAutocompleteProps) {
  const [suggestions, setSuggestions] = useState<Suggestion[]>([]);
  const [isOpen, setIsOpen] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [selectedIndex, setSelectedIndex] = useState<number>(-1);
  const containerRef = useRef<HTMLDivElement>(null);
  const debounceRef = useRef<NodeJS.Timeout | null>(null);

  // Click outside listener to close dropdown
  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (containerRef.current && !containerRef.current.contains(event.target as Node)) {
        setIsOpen(false);
        setSelectedIndex(-1);
      }
    }
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const searchAddresses = async (searchQuery: string) => {
    if (searchQuery.trim().length < 3) {
      setSuggestions([]);
      setSelectedIndex(-1);
      return;
    }

    setIsLoading(true);

    try {
      // Llamar al endpoint proxy local en lugar de directo a Google para evitar CORS y proteger la Key
      const url = `/api/places/autocomplete?input=${encodeURIComponent(searchQuery)}`;

      const res = await fetch(url);
      const data = await res.json();
      
      if (data.status === 'OK' && data.predictions) {
        setSuggestions(data.predictions);
        setIsOpen(true);
        setSelectedIndex(-1);
      } else {
        setSuggestions([]);
        setSelectedIndex(-1);
      }
    } catch (error) {
      console.error('Error fetching addresses from local API:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const val = e.target.value;
    onChange(val);
    onSelectCoordinate(null);
    setSelectedIndex(-1);

    if (val.trim() === '') {
      setSuggestions([]);
      setIsOpen(false);
      return;
    }

    if (debounceRef.current) {
      clearTimeout(debounceRef.current);
    }

    debounceRef.current = setTimeout(() => {
      searchAddresses(val);
    }, 300);
  };

  const handleSelect = async (suggestion: Suggestion) => {
    onChange(suggestion.description);
    setIsOpen(false);
    setSuggestions([]);
    setSelectedIndex(-1);

    // Obtener las coordenadas a través de nuestro endpoint proxy de details
    try {
      const url = `/api/places/details?place_id=${suggestion.place_id}`;
      const res = await fetch(url);
      const data = await res.json();
      if (data.status === 'OK' && data.result?.geometry?.location) {
        const { lat, lng } = data.result.geometry.location;
        onSelectCoordinate({ lat, lng });
      }
    } catch (error) {
      console.error('Error fetching place details from local API:', error);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (!isOpen || suggestions.length === 0) return;

    if (e.key === 'ArrowDown') {
      e.preventDefault();
      setSelectedIndex((prev) => (prev < suggestions.length - 1 ? prev + 1 : 0));
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      setSelectedIndex((prev) => (prev > 0 ? prev - 1 : suggestions.length - 1));
    } else if (e.key === 'Enter' && selectedIndex >= 0 && selectedIndex < suggestions.length) {
      e.preventDefault();
      handleSelect(suggestions[selectedIndex]);
    } else if (e.key === 'Escape') {
      setIsOpen(false);
      setSelectedIndex(-1);
    }
  };

  return (
    <div ref={containerRef} className="relative w-full">
      <div className="relative">
        <input
          type="text"
          id={id}
          required={required}
          placeholder={placeholder}
          value={value}
          onChange={handleInputChange}
          onKeyDown={handleKeyDown}
          className={className}
          autoComplete="off"
          role="combobox"
          aria-autocomplete="list"
          aria-expanded={isOpen && suggestions.length > 0}
          aria-controls={`${id}-suggestions`}
          aria-activedescendant={selectedIndex >= 0 ? `${id}-option-${selectedIndex}` : undefined}
        />
        <div className="absolute right-3 top-1/2 -translate-y-1/2 flex items-center gap-1 text-brand-blue-500 pointer-events-none" aria-hidden="true">
          {isLoading ? (
            <Loader2 className="h-4 w-4 animate-spin" />
          ) : (
            <Search className="h-4 w-4" />
          )}
        </div>
      </div>

      {isOpen && suggestions.length > 0 && (
        <ul
          id={`${id}-suggestions`}
          role="listbox"
          className="absolute z-50 w-full mt-1 bg-brand-blue-500 border border-white/20 rounded-xl max-h-60 overflow-y-auto shadow-2xl text-white divide-y divide-white/10"
        >
          {suggestions.map((s, idx) => {
            const isSelected = idx === selectedIndex;
            return (
              <li
                key={s.place_id}
                id={`${id}-option-${idx}`}
                role="option"
                aria-selected={isSelected}
                onClick={() => handleSelect(s)}
                className={`px-4 py-3 cursor-pointer flex items-start gap-3 transition-colors text-sm ${
                  isSelected ? 'bg-white/10 ring-1 ring-brand-yellow-500' : 'hover:bg-white/10'
                }`}
              >
                <MapPin className="h-5 w-5 text-brand-yellow-500 shrink-0 mt-0.5" aria-hidden="true" />
                <div>
                  <p className="font-semibold text-white">
                    {s.description.split(',')[0]}
                  </p>
                  <p className="text-xs text-brand-blue-50 mt-0.5 line-clamp-1 font-medium">
                    {s.description}
                  </p>
                </div>
              </li>
            );
          })}
        </ul>
      )}
    </div>
  );
}

```

### Componente: `src/components/ui/InputField.tsx`

```tsx
'use client';

import React from 'react';
import { cn } from '@/lib/utils';

export interface InputFieldProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  error?: string | null;
  helpText?: string;
  icon?: React.ReactNode;
  containerClassName?: string;
  labelClassName?: string;
}

/**
 * InputField Component
 * Standardized form input container.
 * Follows DESIGN.md specifications:
 * - Height: h-11 (44px touch target)
 * - Border: border-2 border-brand-blue-100 rounded-xl bg-white
 * - Padding left: pl-10 when icon is present
 * - Label: font-subheading text-xs uppercase tracking-wider text-brand-blue-700
 * - Help text: font-mono text-2xs text-brand-blue-400
 * - Focus: border-brand-blue-700 + ring-2 ring-brand-blue-500/20
 * - Error: border-red-500 + ring-2 ring-red-500/20
 */
export const InputField = React.forwardRef<HTMLInputElement, InputFieldProps>(
  (
    {
      label,
      error,
      helpText,
      icon,
      containerClassName,
      labelClassName,
      className,
      id,
      disabled,
      required,
      ...inputProps
    },
    ref
  ) => {
    const generatedId = React.useId();
    const inputId = id || generatedId;
    const errorId = `${inputId}-error`;
    const helpId = `${inputId}-help`;

    return (
      <div className={cn('input-wrapper flex flex-col gap-1.5 w-full', containerClassName)}>
        {label && (
          <label
            htmlFor={inputId}
            className={cn(
              'input-label font-subheading text-xs uppercase tracking-wider font-bold text-brand-blue-500 flex items-center justify-between',
              labelClassName
            )}
          >
            <span>
              {label}
              {required && <span className="text-red-500 ml-1">*</span>}
            </span>
          </label>
        )}

        <div className="relative flex items-center w-full">
          {icon && (
            <div className="input-icon absolute left-3.5 text-brand-blue-500 pointer-events-none flex items-center justify-center w-5 h-5">
              {icon}
            </div>
          )}

          <input
            ref={ref}
            id={inputId}
            disabled={disabled}
            required={required}
            aria-invalid={!!error}
            aria-describedby={error ? errorId : helpText ? helpId : undefined}
            className={cn(
              'input-field h-11 w-full border-2 rounded-xl bg-white font-sans text-sm text-brand-blue-500 placeholder:text-brand-blue-500 transition-all duration-200 focus:outline-none',
              icon ? 'pl-10 pr-4' : 'px-4',
              error
                ? 'border-red-500 focus:border-red-500 ring-2 ring-red-500/20 text-red-600'
                : 'border-brand-blue-300 hover:border-brand-blue-400 focus:border-brand-blue-500 focus:ring-2 focus:ring-brand-blue-500/20',
              disabled && 'border-brand-blue-100 bg-brand-blue-50/50 text-brand-blue-400 cursor-not-allowed',
              className
            )}
            {...inputProps}
          />
        </div>

        {error ? (
          <p id={errorId} role="alert" className="font-mono text-2xs text-red-600 font-medium">
            {error}
          </p>
        ) : helpText ? (
          <p id={helpId} className="font-mono text-2xs text-brand-blue-500">
            {helpText}
          </p>
        ) : null}
      </div>
    );
  }
);

InputField.displayName = 'InputField';

export default InputField;

```

### Componente: `src/components/cotizar/unified/CotizadorComparativa.tsx`

```tsx
'use client';

import React, { useState } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { AlertTriangle, Zap, Package, Check, ArrowRight, CloudRain } from 'lucide-react';
import { trackAnalytics } from '@/lib/analytics';
import DoubleBezelCard from '@/components/ui/DoubleBezelCard';
import CTANestedPill from '@/components/ui/CTANestedPill';
import RadioCardGroup from '@/components/ui/RadioCardGroup';
import type { ServiceKey, UseCotizadorUnificadoReturn } from '@/hooks/cotizador/useCotizadorUnified';
import {
  EXPRESS_CUTOFF_TIME,
  EXPRESS_LEAD_TIME,
  LOWCOST_CUTOFF_TIME,
  LOWCOST_DELIVERY_DEADLINE,
  STANDARD_WEIGHT_KG,
} from '@/lib/promises';

interface CotizadorComparativaProps {
  form: Pick<
    UseCotizadorUnificadoReturn,
    'resultado' | 'quoteId' | 'getWhatsAppLink' | 'shouldReduceMotion'
  >;
  error: string | null;
}

/**
 * Reglas de entrega de cada servicio. No son decoración: son el compromiso real
 * que el negocio publica y lo que el visitante está eligiendo entre servicios.
 *
 * Ninguno de los dos promete una duración. Express vende una franja de 3 hs que
 * elige el cliente; LowCost, una entrega en el día sin elección de horario. Por eso
 * la comparación de tiempo es una línea del día, no una cuenta regresiva.
 */
const REGLAS: Record<
  ServiceKey,
  {
    nombre: string;
    entrega: string;
    detalle: string;
    /** Horas del día (24 h) que pinta la línea del día. */
    banda: { desde: number; hasta: number; rotulo: string };
    corte: number;
  }
> = {
  express: {
    nombre: 'Express',
    entrega: 'Elegís una franja de 3 hs',
    detalle: `Pedido con ${EXPRESS_LEAD_TIME} y hasta las ${EXPRESS_CUTOFF_TIME}. La franja la elegís vos, por ejemplo de 10 a 13 hs.`,
    banda: { desde: 10, hasta: 13, rotulo: 'Tu franja' },
    corte: 15,
  },
  lowcost: {
    nombre: 'LowCost',
    entrega: `En el día, antes de las ${LOWCOST_DELIVERY_DEADLINE}`,
    detalle: `Sin elección de horario. Pedido antes de las ${LOWCOST_CUTOFF_TIME}, se entrega en el transcurso del día antes de las ${LOWCOST_DELIVERY_DEADLINE}.`,
    banda: { desde: 9, hasta: 19, rotulo: 'En algún momento del día' },
    corte: 13,
  },
};

/** Escala de la línea del día, compartida por los dos servicios: 9 → 19 hs. */
const DIA_DESDE = 9;
const DIA_HASTA = 19;
const MARCAS = [9, 11, 13, 15, 17, 19];
const posicion = (hora: number) => ((hora - DIA_DESDE) / (DIA_HASTA - DIA_DESDE)) * 100;

function precioTexto(precio: number | 'consultar'): string {
  return precio === 'consultar' ? 'A consultar' : `$${precio.toLocaleString('es-AR')}`;
}

export default function CotizadorComparativa({ form, error }: CotizadorComparativaProps) {
  const { resultado, quoteId, getWhatsAppLink, shouldReduceMotion } = form;
  const [elegido, setElegido] = useState<string>('');

  // Sin resultado no hay escala posible: 0 evita NaN en el ancho de las barras.
  const precioExpress = resultado?.express.precio;
  const precioLowCost = resultado?.lowcost.precio;
  const ambosNumericos = typeof precioExpress === 'number' && typeof precioLowCost === 'number';
  const referenciaPrecio = ambosNumericos ? Math.max(precioExpress!, precioLowCost!) : 0;
  const diferenciaPrecio = ambosNumericos ? precioExpress! - precioLowCost! : 0;

  const ambosConsultar =
    resultado !== null &&
    resultado.express.precio === 'consultar' &&
    resultado.lowcost.precio === 'consultar';

  // Opciones para RadioCardGroup
  const serviceOptions = React.useMemo(() => [
    {
      id: 'express',
      label: 'Express',
      description: 'Elegís una franja de 3 hs a elección, en el día.',
      price: resultado?.express.precio ? precioTexto(resultado.express.precio) : '—',
      badge: 'MÁS RÁPIDO',
      serviceType: 'EXPRESS',
      icon: <Zap className="h-6 w-6" aria-hidden="true" />,
      disabled: !resultado || resultado.express.precio === 'consultar',
    },
    {
      id: 'lowcost',
      label: 'LowCost',
      description: `Entrega programada en el día antes de las ${LOWCOST_DELIVERY_DEADLINE}.`,
      price: resultado?.lowcost.precio ? precioTexto(resultado.lowcost.precio) : '—',
      badge: 'MÁS ECONÓMICO',
      serviceType: 'LOW_COST',
      icon: <Package className="h-6 w-6" aria-hidden="true" />,
      disabled: !resultado || resultado.lowcost.precio === 'consultar',
    },
  ], [resultado]);

  const handleServiceChange = (service: string) => {
    const svc = service as ServiceKey;
    setElegido(service);
    trackAnalytics.whatsappClick(`cotizador_unificado_${svc}`);
    // Open WhatsApp link
    if (resultado) {
      const link = getWhatsAppLink(svc);
      if (link !== '#') {
        window.open(link, '_blank', 'noopener,noreferrer');
      }
    }
  };

  return (
    <div className="mt-6 relative z-10 space-y-4">
      <AnimatePresence>
        {error && (
          <motion.div
            role="alert"
            aria-live="assertive"
            initial={shouldReduceMotion ? { opacity: 0 } : { opacity: 0, y: -6 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -6 }}
            className="p-3 bg-red-500/20 border border-red-500/40 rounded-xl flex items-start gap-2 text-red-100 text-xs font-sans"
          >
            <AlertTriangle className="h-4 w-4 shrink-0 mt-0.5 text-red-300" />
            <span>{error}</span>
          </motion.div>
        )}
      </AnimatePresence>

      <AnimatePresence>
        {resultado && (
          <motion.div
            role="region"
            aria-live="polite"
            aria-atomic="true"
            initial={shouldReduceMotion ? { opacity: 0 } : { opacity: 0, y: 12 }}
            animate={shouldReduceMotion ? { opacity: 1 } : { opacity: 1, y: 0 }}
            exit={shouldReduceMotion ? { opacity: 0 } : { opacity: 0, y: -8 }}
            transition={shouldReduceMotion ? { duration: 0.15 } : { type: 'spring', stiffness: 100, damping: 20 }}
            className="w-full"
          >
            <span className="sr-only">
              {ambosConsultar
                ? `Distancia calculada: ${resultado.distancia} kilómetros. Supera el radio estándar de 20 kilómetros, necesita una cotización personalizada.`
                : `Distancia: ${resultado.distancia} kilómetros. Tarifa Express: ${precioTexto(resultado.express.precio)}. Tarifa LowCost: ${precioTexto(resultado.lowcost.precio)}.`}
            </span>

            <DoubleBezelCard>
              <div className="space-y-5">
                {/* Cabecera: la distancia medida, una sola vez */}
                <div className="flex flex-wrap items-center justify-between gap-3 pb-4 border-b border-brand-blue-100">
                  <div>
                    <span className="block text-2xs font-subheading font-bold uppercase tracking-wider text-brand-blue-400">
                      Distancia medida
                    </span>
                    <span className="font-mono text-3xl sm:text-4xl font-bold text-brand-blue-700 tabular-nums tracking-tight">
                      {resultado.distancia} km
                    </span>
                  </div>
                  {quoteId && (
                    <span className="font-mono text-xs px-2.5 py-1 rounded-full bg-brand-blue-50 text-brand-blue-700 border border-brand-blue-100 tabular-nums">
                      #{quoteId}
                    </span>
                  )}
                </div>

                {ambosConsultar ? (
                  <div className="space-y-4">
                    <p className="font-sans text-sm text-brand-blue-700 leading-relaxed">
                      Tu envío supera el radio estándar de 20 km. Las tarifas por zona no alcanzan:
                      pasanos el caso y te pasamos el valor.
                    </p>
                    <CTANestedPill href="/contacto" variant="primary" className="w-full sm:w-auto">
                      Pedir Cotización Personalizada
                    </CTANestedPill>
                  </div>
                ) : (
                  <>
                    {/* ─────────────────────────────────────────────────────────────
                        FILA 1 — LO QUE PAGÁS. Las dos barras salen casi iguales:
                        ese es el dato, no un defecto de la gráfica.
                        ───────────────────────────────────────────────────────────── */}
                    <section aria-labelledby="fila-precio">
                      <h3
                        id="fila-precio"
                        className="font-subheading text-xs uppercase tracking-widest font-bold text-brand-blue-500 mb-3"
                      >
                        Lo que pagás
                      </h3>

                      <div className="space-y-3">
                        {(['express', 'lowcost'] as const).map((key) => {
                          const regla = REGLAS[key];
                          const precio = resultado[key].precio;
                          const ancho =
                            typeof precio === 'number' && referenciaPrecio > 0
                              ? (precio / referenciaPrecio) * 100
                              : 0;

                          return (
                            <div key={key} className="space-y-1.5">
                              <div className="flex items-baseline justify-between gap-3">
                                <span
                                  className={`font-subheading text-xs font-bold uppercase tracking-wider ${
                                    key === 'express' ? 'text-brand-yellow-600' : 'text-brand-blue-500'
                                  }`}
                                >
                                  {regla.nombre}
                                </span>
                                <span className="font-mono text-2xl sm:text-3xl font-bold text-brand-blue-700 tabular-nums">
                                  {precioTexto(precio)}
                                  {typeof precio === 'number' && (
                                    <span className="text-xs font-bold text-brand-blue-400 ml-1">ARS</span>
                                  )}
                                </span>
                              </div>
                              <div
                                role="presentation"
                                className="h-2.5 w-full rounded-full bg-brand-blue-50 overflow-hidden"
                              >
                                <div
                                  className={`h-full rounded-full ${
                                    key === 'express' ? 'bg-brand-yellow-500' : 'bg-brand-blue-500'
                                  }`}
                                  style={{ width: `${ancho}%` }}
                                />
                              </div>
                            </div>
                          );
                        })}
                      </div>

                      {diferenciaPrecio > 0 && (
                        <p className="mt-3 pt-3 border-t border-brand-blue-100 font-sans text-xs text-brand-blue-500">
                          La diferencia entre uno y otro es de{' '}
                          <span className="font-mono font-bold text-brand-blue-700 tabular-nums">
                            ${diferenciaPrecio.toLocaleString('es-AR')}
                          </span>
                          . Lo demás que cambia es cuándo lo recibís.
                        </p>
                      )}
                    </section>

                    {/* ─────────────────────────────────────────────────────────────
                        FILA 2 — CUÁNDO LLEGA. Una línea del día (9 → 19 hs) para
                        los dos: Express ocupa la franja que elegís; LowCost, el día
                        entero. No hay duración que prometer, y no se muestra una.
                        ───────────────────────────────────────────────────────────── */}
                    <section aria-labelledby="fila-tiempo" className="pt-4 border-t border-brand-blue-100">
                      <h3
                        id="fila-tiempo"
                        className="font-subheading text-xs uppercase tracking-widest font-bold text-brand-blue-500 mb-3"
                      >
                        Cuándo llega
                      </h3>

                      <div className="space-y-4">
                        {(['express', 'lowcost'] as const).map((key) => {
                          const regla = REGLAS[key];
                          const esExpress = key === 'express';
                          const izquierda = posicion(regla.banda.desde);
                          const ancho = posicion(regla.banda.hasta) - izquierda;

                          return (
                            <div key={key} className="space-y-1.5">
                              <div className="flex items-baseline justify-between gap-3">
                                <span className="font-sans text-xs text-brand-blue-500">{regla.nombre}</span>
                                <span className="font-sans text-sm font-bold text-brand-blue-700 text-right">
                                  {regla.entrega}
                                </span>
                              </div>

                              {/* Resumen visual del texto de abajo: el lector de
                                  pantalla ya tiene la regla en palabras. */}
                              <div aria-hidden="true" className="relative h-6 rounded-md bg-brand-blue-50">
                                <div
                                  className={`absolute inset-y-0 rounded-md flex items-center px-2 overflow-hidden ${
                                    esExpress
                                      ? 'bg-brand-yellow-500 text-brand-blue-900'
                                      : 'bg-[repeating-linear-gradient(135deg,var(--color-brand-blue-500)_0_6px,var(--color-brand-blue-400)_6px_12px)] text-white'
                                  }`}
                                  style={{ left: `${izquierda}%`, width: `${ancho}%` }}
                                >
                                  <span className="font-subheading text-2xs uppercase tracking-wider font-bold whitespace-nowrap">
                                    {regla.banda.rotulo}
                                  </span>
                                </div>
                                <div
                                  className="absolute -inset-y-1 w-0.5 -translate-x-1/2 bg-brand-blue-700 ring-2 ring-white"
                                  style={{ left: `${posicion(regla.corte)}%` }}
                                />
                              </div>

                              <p className="font-sans text-2xs text-brand-blue-400 leading-snug">
                                {regla.detalle}
                              </p>
                            </div>
                          );
                        })}
                      </div>

                      <div aria-hidden="true" className="relative h-4 font-mono text-2xs text-brand-blue-400 tabular-nums">
                        {MARCAS.map((hora) => (
                          <span
                            key={hora}
                            className="absolute -translate-x-1/2 first:translate-x-0 last:-translate-x-full whitespace-nowrap"
                            style={{ left: `${posicion(hora)}%` }}
                          >
                            {hora} hs
                          </span>
                        ))}
                      </div>
                      <p className="font-sans text-2xs text-brand-blue-400 flex items-center gap-1.5">
                        <span aria-hidden="true" className="inline-block h-3 w-0.5 bg-brand-blue-700" />
                        Horario de corte para pedir en el día.
                      </p>
                    </section>

                    {/* ─────────────────────────────────────────────────────────────
                        LA DECISIÓN. RadioCardGroup para elegir servicio.
                        ───────────────────────────────────────────────────────────── */}
                    <div className="pt-5 border-t border-brand-blue-100">
                      <h3 className="font-subheading text-xs uppercase tracking-widest font-bold text-brand-blue-500 mb-3">
                        Elegí cómo lo querés
                      </h3>

                      <RadioCardGroup
                        name="cotizador-service-selector"
                        value={elegido}
                        onChange={handleServiceChange}
                        options={serviceOptions}
                        gridCols="grid-cols-1 sm:grid-cols-2"
                      />
                    </div>

                    {/* El precio de arriba es por distancia. Lo que pasa en el viaje
                        (lluvia, espera, paradas, bulto grande) suma aparte, y se avisa
                        antes de confirmar, no después. */}
                    <div className="flex items-start gap-3 rounded-xl border border-brand-blue-100 bg-brand-blue-50/60 px-4 py-3.5">
                      <CloudRain className="h-4 w-4 shrink-0 mt-0.5 text-brand-blue-500" aria-hidden="true" />
                      <p className="font-sans text-xs text-brand-blue-700 leading-relaxed">
                        El precio es por distancia, con bulto de hasta {STANDARD_WEIGHT_KG} kg. Lluvia,
                        espera en puerta, paradas extra o un bulto más grande suman recargo.{' '}
                        <a
                          href="#recargos"
                          className="font-bold underline underline-offset-2 decoration-brand-blue-300 hover:decoration-brand-blue-700 focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-blue-500 rounded-sm"
                        >
                          Ver cuáles y cuánto
                        </a>
                      </p>
                    </div>
                  </>
                )}
              </div>
            </DoubleBezelCard>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
```

### Componente: `src/components/ui/DoubleBezelCard.tsx`

```tsx
'use client';

import React from 'react';
import { cn } from '@/lib/utils';

export interface DoubleBezelCardProps extends React.HTMLAttributes<HTMLDivElement> {
  children: React.ReactNode;
  className?: string;
  outerClassName?: string;
  innerClassName?: string;
  variant?: 'light' | 'dark';
  hoverEffect?: boolean;
}

/**
 * DoubleBezelCard Component
 * Signature Two-tier container system (outer bezel + inner card) for primary content.
 * Follows DESIGN.md specifications:
 * - Outer: bg-brand-blue-50/80, border-brand-blue-100, rounded-2xl (16px), p-2 (8px), shadow-float
 * - Inner: bg-white (or brand-blue-700 in dark variant), rounded-xl (12px), p-6, shadow-sm
 * - Hover: shadow-antigravity-deep, border-brand-blue-300
 */
export const DoubleBezelCard = React.forwardRef<HTMLDivElement, DoubleBezelCardProps>(
  (
    {
      children,
      className,
      outerClassName,
      innerClassName,
      variant = 'light',
      hoverEffect = true,
      ...props
    },
    ref
  ) => {
    const isDark = variant === 'dark';

    return (
      <div
        ref={ref}
        className={cn(
          'double-bezel-outer transition-all duration-300 rounded-2xl p-2 shadow-float',
          isDark
            ? 'bg-brand-blue-50/80 border border-brand-blue-100/80'
            : 'bg-brand-blue-50/80 border border-brand-blue-100',
          hoverEffect &&
            (isDark
              ? 'hover:shadow-antigravity-deep hover:border-brand-yellow-400/80'
              : 'hover:shadow-antigravity-deep hover:border-brand-blue-300'),
          outerClassName,
          className
        )}
        {...props}
      >
        <div
          className={cn(
            'double-bezel-inner rounded-xl p-6 shadow-sm overflow-hidden transition-colors duration-200',
            isDark
              ? 'bg-brand-blue-500 border border-white/10 text-white'
              : 'bg-white border border-brand-blue-50/50 text-brand-blue-500',
            innerClassName
          )}
        >
          {children}
        </div>
      </div>
    );
  }
);

DoubleBezelCard.displayName = 'DoubleBezelCard';

export default DoubleBezelCard;

```

### Componente: `src/components/ui/RadioCardGroup.tsx`

```tsx
'use client';

import React from 'react';
import { cn } from '@/lib/utils';
import { Check } from 'lucide-react';

export interface RadioCardOption {
  id: string;
  label: string;
  description?: string;
  price?: string;
  badge?: string;
  serviceType?: 'EXPRESS' | 'LOW_COST' | 'FLEX' | string;
  icon?: React.ReactNode;
  disabled?: boolean;
}

export interface RadioCardGroupProps {
  options: RadioCardOption[];
  value: string;
  onChange: (value: string) => void;
  name?: string;
  className?: string;
  gridCols?: string;
}

/**
 * RadioCardGroup Component
 * Interactive service selection grid with distinct checked states per service type.
 * Follows DESIGN.md specifications:
 * - Grid 3 cols desktop, 1 col mobile
 * - Card: bg-white, border-2 border-brand-blue-100, rounded-xl, p-6
 * - Checked Express: bg-brand-blue-700, border-brand-blue-700, text-white
 * - Checked LowCost: bg-brand-blue-50, border-brand-blue-200, text-brand-blue-700
 * - Checked Flex: bg-brand-yellow-50, border-brand-yellow-200, text-brand-blue-700
 */
export const RadioCardGroup: React.FC<RadioCardGroupProps> = ({
  options,
  value,
  onChange,
  name = 'service-selector',
  className,
  gridCols = 'grid-cols-1 md:grid-cols-3',
}) => {
  return (
    <div
      role="radiogroup"
      aria-label="Selector de servicio"
      className={cn('grid gap-4 w-full', gridCols, className)}
    >
      {options.map((opt) => {
        const isChecked = value === opt.id;
        const type = (opt.serviceType || opt.id).toUpperCase();

        const getCheckedStyles = () => {
          if (type.includes('EXPRESS')) {
            return 'bg-brand-blue-500 border-brand-blue-500 text-white shadow-md';
          }
          if (type.includes('LOW') || type.includes('LOWCOST')) {
            return 'bg-brand-blue-50 border-brand-blue-200 text-brand-blue-500 shadow-sm';
          }
          if (type.includes('FLEX')) {
            return 'bg-brand-yellow-50 border-brand-yellow-200 text-brand-blue-500 shadow-sm';
          }
          return 'bg-brand-blue-500 border-brand-blue-500 text-white shadow-md';
        };

        const uncheckedStyles =
          'bg-white border-2 border-brand-blue-100 text-brand-blue-500 hover:border-brand-blue-200 hover:bg-brand-blue-50/30';

        const checkedStyles = isChecked ? getCheckedStyles() : uncheckedStyles;

        return (
          <label
            key={opt.id}
            role="radio"
            aria-checked={isChecked}
            tabIndex={0}
            onKeyDown={(e) => {
              if (e.key === ' ' || e.key === 'Enter') {
                e.preventDefault();
                if (!opt.disabled) onChange(opt.id);
              }
            }}
            onClick={() => {
              if (!opt.disabled) onChange(opt.id);
            }}
            className={cn(
              'relative flex flex-col justify-between p-6 rounded-xl border-2 transition-[transform,background-color,border-color,box-shadow] duration-200 ease-[cubic-bezier(0.16,1,0.3,1)] cursor-pointer select-none hover:-translate-y-0.5 active:scale-98 focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-blue-500 focus-visible:ring-offset-2',
              checkedStyles,
              opt.disabled && 'opacity-50 cursor-not-allowed pointer-events-none'
            )}
          >
            <input
              type="radio"
              name={name}
              value={opt.id}
              checked={isChecked}
              onChange={() => onChange(opt.id)}
              disabled={opt.disabled}
              className="sr-only"
            />

            <div>
              {/* Card Header: Icon/Badge + Check indicator */}
              <div className="flex items-center justify-between mb-4">
                {opt.icon && (
                  <div
                    className={cn(
                      'w-12 h-12 rounded-xl flex items-center justify-center transition-colors',
                      isChecked && type.includes('EXPRESS')
                        ? 'bg-white/20 text-white'
                        : 'bg-brand-blue-50 text-brand-blue-500 border border-brand-blue-100'
                    )}
                  >
                    {opt.icon}
                  </div>
                )}

                {opt.badge && (
                  <span
                    className={cn(
                      'font-subheading text-2xs uppercase tracking-wider font-bold px-2.5 py-1 rounded-full',
                      isChecked && type.includes('EXPRESS')
                        ? 'bg-brand-yellow-500 text-brand-blue-500'
                        : 'bg-brand-blue-50 text-brand-blue-500'
                    )}
                  >
                    {opt.badge}
                  </span>
                )}

                <div
                  className={cn(
                    'w-6 h-6 rounded-full border-2 flex items-center justify-center ml-auto transition-all',
                    isChecked
                      ? type.includes('EXPRESS')
                        ? 'bg-brand-yellow-500 border-brand-yellow-500 text-brand-blue-500'
                        : 'bg-brand-blue-500 border-brand-blue-500 text-white'
                      : 'border-brand-blue-200 bg-white'
                  )}
                >
                  {isChecked && <Check className="w-3.5 h-3.5 stroke-3" />}
                </div>
              </div>

              {/* Title & Description */}
              <h3
                className={cn(
                  'font-subheading text-xl uppercase tracking-wide font-bold mb-1',
                  isChecked && type.includes('EXPRESS') ? 'text-white' : 'text-brand-blue-500'
                )}
              >
                {opt.label}
              </h3>

              {opt.description && (
                <p
                  className={cn(
                    'text-xs font-sans leading-relaxed',
                    isChecked && type.includes('EXPRESS')
                      ? 'text-brand-blue-50'
                      : 'text-brand-blue-500'
                  )}
                >
                  {opt.description}
                </p>
              )}
            </div>

            {/* Price section if provided */}
            {opt.price && (
              <div className="mt-4 pt-3 border-t border-current/10 flex items-baseline justify-between">
                <span
                  className={cn(
                    'text-2xs font-subheading uppercase tracking-wider',
                    isChecked && type.includes('EXPRESS') ? 'text-brand-blue-50' : 'text-brand-blue-500'
                  )}
                >
                  DESDE
                </span>
                <span
                  className={cn(
                    'font-mono text-lg font-bold tabular-nums',
                    isChecked && type.includes('EXPRESS')
                      ? 'text-brand-yellow-500'
                      : 'text-brand-blue-500'
                  )}
                >
                  {opt.price}
                </span>
              </div>
            )}
          </label>
        );
      })}
    </div>
  );
};

export default RadioCardGroup;

```

### Componente: `src/components/cotizar/unified/CotizadorMapa.tsx`

```tsx
'use client';

import React from 'react';
import DynamicRouteMap from '@/components/ui/DynamicRouteMap';
import type { UseCotizadorUnificadoReturn } from '@/hooks/cotizador/useCotizadorUnified';

interface CotizadorMapaProps {
  form: Pick<UseCotizadorUnificadoReturn, 'origenCoords' | 'destinoCoords' | 'routeCoords' | 'resultado'>;
}

/**
 * La ruta es única: es la misma medición que alimenta las dos tarifas. El pie
 * aclara que el trazado no cambia según el servicio elegido, porque no cambia.
 */
export default function CotizadorMapa({ form }: CotizadorMapaProps) {
  const { origenCoords, destinoCoords, routeCoords, resultado } = form;

  return (
    <div className="lg:col-span-5 min-h-90 lg:min-h-full rounded-[28px] sm:rounded-[30px] bg-white/10 backdrop-blur-md border border-white/20 p-2.5 shadow-xl">
      <div className="bg-brand-blue-900 p-6 rounded-[20px] border border-white/10 flex flex-col justify-between h-full relative overflow-hidden text-white">
        <div className="absolute inset-0 opacity-10 bg-[linear-gradient(to_right,#ffffff_1px,transparent_1px),linear-gradient(to_bottom,#ffffff_1px,transparent_1px)] bg-size-[24px_24px] pointer-events-none" />

        <div className="relative z-10 flex justify-between items-center border-b border-white/15 pb-3 mb-3">
          <div className="flex items-center gap-2">
            <div className="w-2.5 h-2.5 rounded-full bg-brand-yellow-500 motion-safe:animate-ping" />
            <span className="text-xs font-mono text-brand-yellow-500 uppercase tracking-widest font-semibold tabular-nums">
              Midiendo ruta
            </span>
          </div>
          <span className="text-2xs font-mono text-white/90 tabular-nums">
            OpenStreetMap + OSRM
          </span>
        </div>

        <div className="relative grow min-h-65 rounded-xl overflow-hidden border border-white/15 shadow-inner z-10">
          <DynamicRouteMap
            origin={origenCoords}
            destination={destinoCoords}
            routeCoords={routeCoords}
            distanceKm={resultado?.distancia}
            serviceType="EXPRESS"
          />
        </div>

        <div className="relative z-10 text-2xs font-mono text-white/90 space-y-1.5 border-t border-white/15 pt-3 mt-3 tabular-nums">
          <div className="flex justify-between gap-3">
            <span>Distancia:</span>
            <span className="text-white">
              {resultado ? `${resultado.distancia} km` : 'Pendiente'}
            </span>
          </div>
          <div className="flex justify-between gap-3">
            <span>Tarifa:</span>
            <span className="text-brand-yellow-500 font-bold uppercase">Express + LowCost</span>
          </div>
          <div className="flex justify-between gap-3">
            <span>Cobertura:</span>
            <span className="text-white">Todo Mar del Plata</span>
          </div>
        </div>
      </div>
    </div>
  );
}

```

### Componente: `src/components/ui/DynamicRouteMap.tsx`

```tsx
'use client';

import React from 'react';
import dynamic from 'next/dynamic';

const LeafletRouteMap = dynamic(() => import('./LeafletRouteMap'), {
  ssr: false,
  loading: () => (
    <div className="w-full h-full min-h-75 bg-brand-blue-500 flex items-center justify-center rounded-3xl border border-white/10 animate-pulse">
      <div className="text-center space-y-2">
        <svg className="animate-spin h-8 w-8 text-brand-yellow mx-auto" fill="none" viewBox="0 0 24 24">
          <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
          <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
        </svg>
        <span className="text-xs font-mono text-brand-blue-100">Cargando mapa interactivo...</span>
      </div>
    </div>
  ),
});

interface Coordinate {
  lat: number;
  lng: number;
}

interface DynamicRouteMapProps {
  origin: Coordinate | null;
  destination: Coordinate | null;
  routeCoords: [number, number][];
  distanceKm?: number;
  serviceType?: 'EXPRESS' | 'LOW_COST';
}

export default function DynamicRouteMap(props: DynamicRouteMapProps) {
  return <LeafletRouteMap {...props} />;
}

```

### Componente: `src/components/cotizar/unified/CotizadorGuia.tsx`

```tsx
'use client';

import React from 'react';
import { MapPin, GitCompareArrows, MessageCircle } from 'lucide-react';

const PASOS = [
  {
    n: '01',
    icon: MapPin,
    titulo: 'Cargá el envío',
    detalle: 'Retiro, entrega y tus datos de contacto.',
  },
  {
    n: '02',
    icon: GitCompareArrows,
    titulo: 'Compará las dos tarifas',
    detalle: 'Precio y horario de entrega de cada servicio, lado a lado.',
  },
  {
    n: '03',
    icon: MessageCircle,
    titulo: 'Elegí y confirmá',
    detalle: 'Te pasamos el pedido armado por WhatsApp.',
  },
];

/**
 * Riel de orientación de la guía. Es una secuencia real —el orden importa porque
 * cada paso habilita el siguiente—, por eso lleva numeración. Se muestra siempre
 * arriba, incluso con resultados en pantalla, para no perder el hilo.
 */
export default function CotizadorGuia() {
  return (
    <nav aria-label="Cómo funciona el cotizador" className="w-full">
      <ol className="grid grid-cols-1 sm:grid-cols-3 gap-3 sm:gap-4">
        {PASOS.map((paso) => (
          <li
            key={paso.n}
            className="flex items-start gap-3 rounded-xl border border-white/15 bg-white/5 px-4 py-3.5"
          >
            <span className="font-mono text-xs text-brand-yellow-500 tabular-nums shrink-0 pt-0.5">
              {paso.n}
            </span>
            <span className="min-w-0">
              <span className="flex items-center gap-1.5 font-subheading text-xs uppercase font-bold tracking-wider text-white">
                <paso.icon className="h-3.5 w-3.5 text-brand-yellow-500 shrink-0" aria-hidden="true" />
                {paso.titulo}
              </span>
              <span className="block font-sans text-xs text-white/70 mt-1 leading-snug">
                {paso.detalle}
              </span>
            </span>
          </li>
        ))}
      </ol>
    </nav>
  );
}

```

### Componente: `src/components/cotizar/unified/CotizadorRecargos.tsx`

```tsx
import React from 'react';
import {
  BULK_EXTRA_FROM_ARS,
  EXTRA_STOP_MAX_DETOUR_KM,
  EXTRA_STOP_SURCHARGE_PERCENT,
  PERIPHERY_PRICE_PER_KM,
  RAIN_SURCHARGE_PERCENT,
  RAIN_SURCHARGE_PERCENT_EXPRESS_LOWCOST,
  RETRY_CHARGE_PERCENT,
  STANDARD_BULLET_DIMENSIONS_CM,
  STANDARD_WEIGHT_KG,
  WAIT_CHARGE_ARS,
  WAIT_CHARGE_BLOCK_MIN,
  WAIT_TOLERANCE_MIN,
} from '@/lib/promises';

const formatArs = (value: number) => `$${value.toLocaleString('es-AR')}`;

/**
 * Lo que el cotizador no suma solo. El precio de arriba es por distancia; estos
 * recargos dependen de lo que pase en el viaje, así que se informan antes de
 * confirmar en vez de aparecer después. Todos los valores salen de `promises.ts`.
 */
const RECARGOS: { situacion: string; costo: string; detalle: string }[] = [
  {
    situacion: 'Lluvia o calzada mojada',
    costo: `+${RAIN_SURCHARGE_PERCENT_EXPRESS_LOWCOST} %`,
    detalle: `Sobre la tarifa Express o LowCost. En Flex y cuentas corrientes es ${RAIN_SURCHARGE_PERCENT} %.`,
  },
  {
    situacion: 'Espera en puerta',
    costo: `${formatArs(WAIT_CHARGE_ARS)} cada ${WAIT_CHARGE_BLOCK_MIN} min`,
    detalle: `Los primeros ${WAIT_TOLERANCE_MIN} minutos no se cobran. Corre desde el minuto ${WAIT_TOLERANCE_MIN + 1}.`,
  },
  {
    situacion: 'Parada extra en el camino',
    costo: `+${EXTRA_STOP_SURCHARGE_PERCENT} % por parada`,
    detalle: `Si la parada queda sobre la ruta, hasta ${EXTRA_STOP_MAX_DETOUR_KM} km. Si desvía más, es un envío aparte.`,
  },
  {
    situacion: 'Destinatario ausente',
    costo: `${RETRY_CHARGE_PERCENT} % del envío`,
    detalle: 'La segunda visita se cobra como un envío nuevo. En zonas cercanas, a veces la hacemos sin cargo.',
  },
  {
    situacion: `Bulto de más de ${STANDARD_WEIGHT_KG} kg o ${STANDARD_BULLET_DIMENSIONS_CM}`,
    costo: `Desde ${formatArs(BULK_EXTRA_FROM_ARS)}`,
    detalle: 'El monto final depende del servicio. Si el bulto excede ese tamaño, escribinos y lo coordinamos.',
  },
  {
    situacion: 'Destino fuera de la ciudad',
    costo: `${formatArs(PERIPHERY_PRICE_PER_KM)} por km de ruta`,
    detalle: 'Batán, Sierra de los Padres y otras localidades cercanas. Se cotiza por WhatsApp.',
  },
];

export default function CotizadorRecargos() {
  return (
    <section id="recargos" aria-labelledby="recargos-titulo" className="space-y-5 scroll-mt-24">
      <div className="space-y-2">
        <h2
          id="recargos-titulo"
          className="font-display text-2xl sm:text-3xl uppercase tracking-tight text-white"
        >
          Lo que puede sumar al precio
        </h2>
        <p className="font-sans text-white/90 leading-relaxed max-w-3xl text-sm sm:text-base">
          El cotizador calcula el viaje por distancia. Estas situaciones se cobran aparte,
          según lo que pase en el viaje.
        </p>
      </div>

      <dl className="rounded-2xl border border-white/15 bg-white/5 backdrop-blur-md divide-y divide-white/10">
        {RECARGOS.map((recargo) => (
          <div
            key={recargo.situacion}
            className="grid gap-1 sm:grid-cols-12 sm:gap-6 px-4 sm:px-5 py-4"
          >
            <dt className="sm:col-span-4 font-subheading text-sm uppercase tracking-wider text-white">
              {recargo.situacion}
            </dt>
            <dd className="sm:col-span-3 font-mono text-sm font-bold text-brand-yellow-500 tabular-nums">
              {recargo.costo}
            </dd>
            <dd className="sm:col-span-5 font-sans text-sm text-white/85 leading-relaxed">
              {recargo.detalle}
            </dd>
          </div>
        ))}
      </dl>
    </section>
  );
}

```

---

## 3. Estructura de Layout Compartido y Estilos Globales

### Global CSS Styles & Design Tokens (`src/app/globals.css`)

```css
@import "tailwindcss";

/* Tailwind CSS v4 Custom Variant */
@custom-variant dark (&:where(.dark, .dark *));

:root {
  /* ========================================================================
   * SUPERFICIES Y ACCIONES (fuera de @theme para no chocar con text-* font-size)
   * ======================================================================== */
  --surface-page: var(--color-white);
  --surface-card: var(--color-white);
  --surface-muted: var(--color-brand-blue-50);
  --surface-invert: var(--color-brand-blue-700);
  --surface-glass: rgba(255, 255, 255, 0.06);
  --text-body: var(--color-brand-blue-900);
  --text-muted: var(--color-brand-blue-400);
  --text-heading: var(--color-brand-blue-900);
  --text-on-invert: var(--color-white);
  --text-on-accent: var(--color-brand-blue-900);
  --border-subtle: var(--color-brand-blue-100);
  --focus-ring: var(--color-brand-blue-500);
  --action-primary: var(--color-brand-blue-700);
  --action-primary-hover: var(--color-brand-blue-800);
  --action-accent: var(--color-brand-yellow-500);
  --action-accent-hover: var(--color-brand-yellow-400);
  --action-danger: #EF4444;
}

@theme {
  /* ========================================================================
   * PALETA CANÓNICA — Ley de Tres Colores (Ajuste Max #0950F6)
   * Cada token tiene un hex literal. Nada más oscuro que #0950F6.
   * ======================================================================== */

  /* Azul Vibrante — 6 pasos (50 → 500). 500/600/700/900/950 colapsan a #0950F6. */
  --color-brand-blue-50: #E6EEFE;   /* fondo suave, bezel exterior /80, skeleton, hover ghost */
  --color-brand-blue-100: #BACEFD;  /* borde estructural, divisores, stepper línea pendiente */
  --color-brand-blue-200: #8EAFFB;  /* hover borde tarjeta, anillo radio pendiente, trazos SVG */
  --color-brand-blue-300: #628FF9;  /* borde input reposo, hover bezel, trazos SVG secundarios */
  --color-brand-blue-400: #3570F8;  /* íconos, texto grande muted (≥24px). Falla AA en texto normal */
  --color-brand-blue-500: #0950F6;  /* anillo de foco, primario canónico */

  /* Colapsados al tope #0950F6 — el nombre elige la FUNCIÓN, no la oscuridad */
  --color-brand-blue-600: #0950F6;  /* colapsado al tope */
  --color-brand-blue-700: #0950F6;  /* PRIMARIO: lienzo institucional, header, footer, hero, H1/H2 */
  --color-brand-blue-800: #3570F8;  /* hover de FONDOS azules (se aclara porque no se puede oscurecer) */
  --color-brand-blue-900: #0950F6;  /* texto sobre amarillo y cuerpo en tarjetas (4.9:1) */
  --color-brand-blue-950: #0950F6;  /* colapsado al tope (footer profundo = mismo azul) */

  /* Amarillo Vial — 7 pasos (50 → 600). Señal, nunca superficie. ≤15% cobertura. */
  --color-brand-yellow-50: #FFFDE6;  /* fondo Flex seleccionado */
  --color-brand-yellow-100: #FFFAB8; /* badge flex, anillo step completado, halos */
  --color-brand-yellow-200: #FFF78A; /* borde Flex seleccionado */
  --color-brand-yellow-300: #FFF45C; /* detalle mono sobre azul */
  --color-brand-yellow-400: #FFF12E; /* hover CTA primario y WhatsApp */
  --color-brand-yellow-500: #FFEC01; /* CTA primario, step completado/activo, precio sobre azul, franja footer 6px */
  --color-brand-yellow-600: #E6D400; /* pressed del CTA */

  /* Blanco — lienzo único */
  --color-white: #FFFFFF;

  /* ========================================================================
   * ALIAS SEMÁNTICOS CANÓNICOS (referencian a la paleta de arriba)
   * ======================================================================== */
  --color-brand-blue: var(--color-brand-blue-700);
  --color-brand-yellow: var(--color-brand-yellow-500);
  --color-brand-ink: var(--color-brand-blue-900);
  --color-brand-white: var(--color-white);

  /* ========================================================================
   * REDES DE SEGURIDAD: escalas remapeadas a marca (no son API válida)
   * Código nuevo usa solo brand-*. Estas evitan que clases heredadas rompan.
   * ======================================================================== */
  --color-blue-50: var(--color-brand-blue-50);
  --color-blue-100: var(--color-brand-blue-100);
  --color-blue-200: var(--color-brand-blue-200);
  --color-blue-300: var(--color-brand-blue-300);
  --color-blue-400: var(--color-brand-blue-400);
  --color-blue-500: var(--color-brand-blue-500);
  --color-blue-600: var(--color-brand-blue-500);
  --color-blue-700: var(--color-brand-blue-700);
  --color-blue-800: var(--color-brand-blue-400);
  --color-blue-900: var(--color-brand-blue-700);
  --color-blue-950: var(--color-brand-blue-700);

  --color-gray-50: var(--color-white);
  --color-gray-100: var(--color-brand-blue-50);
  --color-gray-200: var(--color-brand-blue-100);
  --color-gray-300: var(--color-brand-blue-200);
  --color-gray-400: var(--color-brand-blue-300);
  --color-gray-500: var(--color-brand-blue-400);
  --color-gray-600: var(--color-brand-blue-500);
  --color-gray-700: var(--color-brand-blue-700);
  --color-gray-800: var(--color-brand-blue-700);
  --color-gray-900: var(--color-brand-blue-700);
  --color-gray-950: var(--color-brand-blue-700);

  --color-slate-50: var(--color-white);
  --color-slate-100: var(--color-brand-blue-50);
  --color-slate-200: var(--color-brand-blue-100);
  --color-slate-300: var(--color-brand-blue-200);
  --color-slate-400: var(--color-brand-blue-300);
  --color-slate-500: var(--color-brand-blue-400);
  --color-slate-600: var(--color-brand-blue-500);
  --color-slate-700: var(--color-brand-blue-700);
  --color-slate-800: var(--color-brand-blue-700);
  --color-slate-900: var(--color-brand-blue-700);
  --color-slate-950: var(--color-brand-blue-700);

  --color-zinc-50: var(--color-white);
  --color-zinc-100: var(--color-brand-blue-50);
  --color-zinc-200: var(--color-brand-blue-100);
  --color-zinc-300: var(--color-brand-blue-200);
  --color-zinc-400: var(--color-brand-blue-300);
  --color-zinc-500: var(--color-brand-blue-400);
  --color-zinc-600: var(--color-brand-blue-500);
  --color-zinc-700: var(--color-brand-blue-700);
  --color-zinc-800: var(--color-brand-blue-700);
  --color-zinc-900: var(--color-brand-blue-700);
  --color-zinc-950: var(--color-brand-blue-700);

  /* ========================================================================
   * NEUTRALIZACIÓN DE PALETAS PROHIBIDAS (Tailwind defaults)
   * Se ponen a `initial` para que no generen CSS. Confirmado: 0 usos en src/.
   * ======================================================================== */
  --color-neutral-50: initial; --color-neutral-100: initial; --color-neutral-200: initial;
  --color-neutral-300: initial; --color-neutral-400: initial; --color-neutral-500: initial;
  --color-neutral-600: initial; --color-neutral-700: initial; --color-neutral-800: initial;
  --color-neutral-900: initial; --color-neutral-950: initial;

  --color-stone-50: initial; --color-stone-100: initial; --color-stone-200: initial;
  --color-stone-300: initial; --color-stone-400: initial; --color-stone-500: initial;
  --color-stone-600: initial; --color-stone-700: initial; --color-stone-800: initial;
  --color-stone-900: initial; --color-stone-950: initial;

  --color-green-50: initial; --color-green-100: initial; --color-green-200: initial;
  --color-green-300: initial; --color-green-400: initial; --color-green-500: initial;
  --color-green-600: initial; --color-green-700: initial; --color-green-800: initial;
  --color-green-900: initial; --color-green-950: initial;

  --color-emerald-50: initial; --color-emerald-100: initial; --color-emerald-200: initial;
  --color-emerald-300: initial; --color-emerald-400: initial; --color-emerald-500: initial;
  --color-emerald-600: initial; --color-emerald-700: initial; --color-emerald-800: initial;
  --color-emerald-900: initial; --color-emerald-950: initial;

  --color-lime-50: initial; --color-lime-100: initial; --color-lime-200: initial;
  --color-lime-300: initial; --color-lime-400: initial; --color-lime-500: initial;
  --color-lime-600: initial; --color-lime-700: initial; --color-lime-800: initial;
  --color-lime-900: initial; --color-lime-950: initial;

  --color-teal-50: initial; --color-teal-100: initial; --color-teal-200: initial;
  --color-teal-300: initial; --color-teal-400: initial; --color-teal-500: initial;
  --color-teal-600: initial; --color-teal-700: initial; --color-teal-800: initial;
  --color-teal-900: initial; --color-teal-950: initial;

  --color-blue-50: initial; --color-blue-100: initial; --color-blue-200: initial;
  --color-blue-300: initial; --color-blue-400: initial; --color-blue-500: initial;
  --color-blue-600: initial; --color-blue-700: initial; --color-blue-800: initial;
  --color-blue-900: initial; --color-blue-950: initial;

  /* ========================================================================
   * TIPOGRAFÍAS OFICIALES — Anton, Bebas Neue, Outfit, Geist Mono
   * ======================================================================== */
  --font-sans: var(--font-sans, "Outfit"), "IBM Plex Sans", sans-serif;
  --font-display: var(--font-display, "Anton SC"), "Anton", sans-serif;
  --font-subheading: var(--font-subheading, "Bebas Neue"), sans-serif;
  --font-mono: var(--font-mono, "Geist Mono"), monospace;

  --text-2xs: 0.625rem;
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  --text-2xl: 1.5rem;
  --text-3xl: 1.875rem;
  --text-4xl: 2.25rem;
  --text-5xl: 3rem;
  --text-6xl: 3.75rem;
  --text-7xl: 4.5rem;
  --text-8xl: 6rem;
  --text-9xl: 9rem;

  --leading-hero: 0.8;
  --leading-none: 1;
  --leading-tight: 1.25;
  --leading-relaxed: 1.625;

  --tracking-tighter: -0.05em;
  --tracking-tight: -0.025em;
  --tracking-normal: 0em;
  --tracking-wide: 0.025em;
  --tracking-wider: 0.05em;
  --tracking-widest: 0.1em;
  --tracking-mega: 0.2em;

  --spacing-section-y: 6rem;
  --spacing-section-y-tight: 3rem;
  --spacing-container-max: 80rem;
  --spacing-control-sm: 2.25rem;
  --spacing-control: 2.5rem;
  --spacing-control-lg: 2.75rem;
  --spacing-control-xl: 3.5rem;
  --spacing-control-2xl: 4rem;

  --radius-sm: 6px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
  --radius-2xl: 24px;
  --radius-3xl: 32px;
  --radius-4xl: 40px;
  --radius-full: 9999px;

  /* ========================================================================
   * SOMBRAS TEÑIDAS — tope #0950F6 / #FFEC01 — NUNCA grises/negras
   * ======================================================================== */
  --shadow-xs: 0 1px 2px rgba(9, 80, 246, 0.04);
  --shadow-sm: 0 2px 4px rgba(9, 80, 246, 0.06), 0 1px 2px rgba(9, 80, 246, 0.03);
  --shadow-md: 0 4px 8px rgba(9, 80, 246, 0.08), 0 2px 4px rgba(9, 80, 246, 0.04);
  --shadow-lg: 0 8px 16px rgba(9, 80, 246, 0.1), 0 4px 8px rgba(9, 80, 246, 0.06);
  --shadow-xl: 0 16px 32px rgba(9, 80, 246, 0.12), 0 8px 16px rgba(9, 80, 246, 0.08);
  --shadow-2xl: 0 25px 50px -12px rgba(9, 80, 246, 0.25);

  --shadow-panel: 0 32px 120px -20px rgba(9, 80, 246, 0.15);
  --shadow-float: 0 25px 50px -12px rgba(9, 80, 246, 0.15);
  --shadow-elevated: 0 16px 40px rgba(9, 80, 246, 0.18);
  --shadow-hover-lift: 0 24px 64px rgba(9, 80, 246, 0.20);
  --shadow-antigravity-deep: 0 24px 64px rgba(9, 80, 246, 0.22);
  --shadow-ambient-elevation: 0 20px 80px rgba(9, 80, 246, 0.18);

  --shadow-accent: 0 12px 40px -6px rgba(255, 236, 1, 0.3);
  --shadow-accent-hover: 0 6px 25px rgba(255, 236, 1, 0.4);
  --shadow-accent-sm: 0 2px 4px rgba(255, 236, 1, 0.15);
  --shadow-accent-md: 0 4px 8px rgba(255, 236, 1, 0.2);
  --shadow-glow-blue: 0 0 25px rgba(9, 80, 246, 0.35);
  --shadow-glow-yellow: 0 0 25px rgba(255, 241, 46, 0.45);
  --shadow-cta-glow: 0 0 28px rgba(255, 236, 1, 0.45), 0 8px 24px rgba(9, 80, 246, 0.18);

  --animate-float-slow: float-slow 6s ease-in-out infinite;
  --animate-pulse-subtle: pulse-subtle 2s ease-in-out infinite;
  --animate-border-pulse: border-pulse 2s ease-in-out infinite;
  --animate-shimmer: shimmer 2.5s ease-in-out infinite;
  --animate-counter-up: counter-up 0.6s ease-out;
  --animate-logos-scroll: marquee-left 30s linear infinite;

  /* ========================================================================
   * DEPRECADO: alias temporales, se borran en la fase 3
   * Cada alias apunta al canónico con var(), NUNCA a un hex.
   * ======================================================================== */
  --color-brand-navy: var(--color-brand-blue-700);
  --color-brand-blue-deep: var(--color-brand-blue-700);
  --color-brand-blue-ink: var(--color-brand-blue-700);
  --color-brand-dark: var(--color-brand-blue-700);
  --color-brand-white-50: var(--color-white);
}

@keyframes float-slow { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-8px); } }
@keyframes pulse-subtle { 0%, 100% { opacity: 1; } 50% { opacity: 0.8; } }
@keyframes border-pulse { 0%, 100% { border-color: rgba(9,80,246,0.2); } 50% { border-color: rgba(9,80,246,0.4); } }
@keyframes shimmer { 0% { background-position: -200% 0; } 100% { background-position: 200% 0; } }
@keyframes counter-up { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }

body {
  font-family: var(--font-sans);
  background-color: var(--surface-page);
  color: var(--text-body);
}

@utility font-display {
  font-family: var(--font-display);
  text-transform: uppercase;
  line-height: 0.9;
  letter-spacing: -0.05em;
  text-wrap: balance;
}

@utility font-subheading {
  font-family: var(--font-subheading);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

@utility font-mono {
  font-family: var(--font-mono);
  font-variant-numeric: tabular-nums;
}

/* Double-Bezel - Firma geométrica oficial */
@utility double-bezel-outer {
  background-color: color-mix(in srgb, var(--color-brand-blue-50) 80%, transparent);
  border: 1px solid var(--color-brand-blue-100);
  padding: 0.5rem;
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-float);
  transition: border-color 0.3s cubic-bezier(0.25,1,0.5,1), box-shadow 0.3s cubic-bezier(0.25,1,0.5,1);
  &:hover { border-color: var(--color-brand-blue-300); box-shadow: var(--shadow-antigravity-deep); }
}
@utility double-bezel-inner {
  background-color: var(--color-white);
  border-radius: var(--radius-lg);
  box-shadow: inset 0 2px 4px rgba(9,80,246,0.06);
  border: 1px solid color-mix(in srgb, var(--color-brand-blue-50) 50%, transparent);
}

/* CTA Nested Pill - Oficial: solo estructura (layout, tipografía, easing).
 * El color (fondo, texto, borde, sombra) lo define el variant del componente.
 */
@utility cta-nested-pill {
  display: inline-flex;
  align-items: center;
  justify-content: space-between;
  border-radius: var(--radius-full);
  font-family: var(--font-subheading);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  font-weight: 700;
  padding: 0.75rem 1.5rem;
  min-height: 56px;
  transition: transform 0.25s cubic-bezier(0.25,1,0.5,1), background-color 0.25s cubic-bezier(0.25,1,0.5,1), border-color 0.25s cubic-bezier(0.25,1,0.5,1), box-shadow 0.25s cubic-bezier(0.25,1,0.5,1);
  &:hover { transform: translateY(-1px); }
  &:active { transform: scale(0.98); }
}
@utility cta-nested-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius-full);
  width: 2.5rem;
  height: 2.5rem;
  margin-left: 0.75rem;
  background-color: rgba(9,80,246,0.1);
  transition: transform 0.25s;
  .group:hover & { transform: translateX(4px); }
}

@utility text-display {
  font-family: var(--font-display);
  font-size: clamp(3rem, 5vw, 4.5rem);
  line-height: 0.85;
  letter-spacing: -0.05em;
  text-wrap: balance;
  text-transform: uppercase;
}
@utility text-h1 {
  font-family: var(--font-display);
  font-size: clamp(2.25rem, 4vw, 3rem);
  line-height: 0.9;
  letter-spacing: -0.025em;
  text-wrap: balance;
  text-transform: uppercase;
}
@utility text-h2 {
  font-family: var(--font-display);
  font-size: clamp(1.75rem, 3vw, 2.25rem);
  line-height: 0.9;
  letter-spacing: -0.02em;
  text-wrap: balance;
  text-transform: uppercase;
}

@utility kinetic-font-stretch {
  display: inline-block;
  transition: transform 0.4s cubic-bezier(0.25,1,0.5,1), letter-spacing 0.4s;
  transform-origin: left;
  &:hover { transform: scaleX(1.08); letter-spacing: 0.02em; }
}

/* V2 Marquee Flotante */
@keyframes marquee-left { from { transform: translateX(0); } to { transform: translateX(-50%); } }
@keyframes marquee-right { from { transform: translateX(-50%); } to { transform: translateX(0); } }

/* Motion compartido de heroes (2026-09) */
@keyframes radar { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
@keyframes floaty {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}
@keyframes shuttle {
  from { transform: translateX(0); }
  to { transform: translateX(100%); }
}
@keyframes draw {
  from { stroke-dashoffset: var(--draw-len, 1200); }
  to { stroke-dashoffset: 0; }
}
@keyframes pulse-ring {
  0% { transform: translate(-50%, -50%) scale(0.6); opacity: 0.9; }
  100% { transform: translate(-50%, -50%) scale(3.2); opacity: 0; }
}
@keyframes roundtrip {
  0% { transform: translateX(0); }
  44% { transform: translateX(100%); }
  56% { transform: translateX(100%); }
  100% { transform: translateX(0); }
}

@utility animate-radar { animation: radar 6s linear infinite; }
@utility animate-floaty { animation: floaty 5s ease-in-out infinite; }
@utility animate-road { animation: marquee-left 3.5s linear infinite; }
@utility animate-shuttle {
  animation: shuttle 5s cubic-bezier(0.45, 0, 0.55, 1) infinite alternate;
}
@utility animate-draw { animation: draw 2.4s cubic-bezier(0.25,1,0.5,1) forwards; }
@utility animate-pulse-ring {
  animation: pulse-ring 3.2s cubic-bezier(0.25, 1, 0.5, 1) infinite;
}
@utility animate-roundtrip {
  animation: roundtrip 4.8s cubic-bezier(0.45, 0, 0.55, 1) infinite;
}
@keyframes grow-x {
  from { transform: scaleX(0); }
  to { transform: scaleX(1); }
}
@utility animate-grow-x {
  animation: grow-x 1.1s cubic-bezier(0.25, 1, 0.5, 1) forwards;
  transform-origin: left center;
}

@utility animate-marquee-left { animation: marquee-left 36s linear infinite; }
@utility animate-marquee-right { animation: marquee-right 42s linear infinite; }
@utility is-paused { animation-play-state: paused !important; }
@utility no-scrollbar { &::-webkit-scrollbar { display: none; } scrollbar-width: none; }

@media (prefers-reduced-motion: reduce) {
  .animate-radar, .animate-floaty, .animate-road, .animate-shuttle, .animate-draw, .animate-roundtrip, .animate-pulse-ring, .animate-grow-x, .animate-marquee-left, .animate-marquee-right {
    animation: none !important;
  }
  .animate-draw { stroke-dashoffset: 0 !important; }
  .animate-grow-x { transform: scaleX(1) !important; }
  .animate-pulse-ring { opacity: 0 !important; }
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}

```

### Root Layout (src/app/layout.tsx) (`src/app/layout.tsx`)

```tsx
import type { Metadata } from 'next';
import { Outfit, Anton, Bebas_Neue, Geist_Mono } from 'next/font/google';
import Script from 'next/script';
import { MotionConfig } from 'motion/react';
import './globals.css';
import ClientLayout from '@/components/ClientLayout';

const outfit = Outfit({
  subsets: ['latin'],
  variable: '--font-sans',
  display: 'swap',
  preload: true,
});

const anton = Anton({
  weight: '400',
  subsets: ['latin'],
  variable: '--font-display',
  display: 'swap',
  preload: true,
});

const bebasNeue = Bebas_Neue({
  weight: '400',
  subsets: ['latin'],
  variable: '--font-subheading',
  display: 'swap',
  preload: true,
});

const geistMono = Geist_Mono({
  subsets: ['latin'],
  variable: '--font-mono',
  display: 'swap',
  preload: true,
});

const baseUrl = 'https://www.enviosdosruedas.com';

export const metadata: Metadata = {
  metadataBase: new URL(baseUrl),
  title: {
    default: 'Mensajería en moto en Mar del Plata | Envíos DosRuedas',
    template: '%s | Envíos DosRuedas',
  },
  description: 'Mensajería en moto y logística e-commerce en Mar del Plata. Express en franja de 3 hs a elección, Mercado Envíos Flex en el día y LowCost para comercios y particulares.',
  authors: [{ name: 'Envíos DosRuedas' }],
  creator: 'Envíos DosRuedas',
  publisher: 'Envíos DosRuedas',
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-video-preview': -1,
      'max-image-preview': 'large',
      'max-snippet': -1,
    },
  },
  openGraph: {
    type: 'website',
    locale: 'es_AR',
    url: baseUrl,
    siteName: 'Envíos DosRuedas',
    title: 'Mensajería en moto en Mar del Plata | Envíos DosRuedas',
    description: 'La solución logística y última milla de mayor confianza en Mar del Plata. Envíos Express, MercadoLibre Flex, ruteo eficiente y cadetería inteligente.',
    images: [
      {
        url: `${baseUrl}/og-image.jpg`,
        width: 1200,
        height: 630,
        alt: 'Envíos DosRuedas - Logística y Mensajería en Mar del Plata',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Mensajería en moto en Mar del Plata | Envíos DosRuedas',
    description: 'La solución logística y última milla de mayor confianza en Mar del Plata.',
    images: [`${baseUrl}/og-image.jpg`],
    creator: '@enviosdosruedas',
  },
  verification: {
    google: ['RKKz8Z6gsm6k3099W3s-xs7G6LTSQQNHpBs_iWfIQnM'],
  },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html
      lang="es"
      className={`${outfit.variable} ${anton.variable} ${bebasNeue.variable} ${geistMono.variable} scroll-smooth`}
      data-scroll-behavior="smooth"
      suppressHydrationWarning
    >
      <head>
        <link rel="preconnect" href="https://www.googletagmanager.com" crossOrigin="anonymous" />
        <link rel="dns-prefetch" href="https://www.googletagmanager.com" />
        <link rel="dns-prefetch" href="https://wa.me" />
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify({
              '@context': 'https://schema.org',
              '@graph': [
                {
                  '@type': 'Organization',
                  name: 'Envíos DosRuedas',
                  url: baseUrl,
                  logo: `${baseUrl}/logo-envios-simplified.webp`,
                  sameAs: [
                    'https://www.instagram.com/enviosdosruedas',
                    'https://www.facebook.com/enviosdosruedas',
                  ],
                  contactPoint: {
                    '@type': 'ContactPoint',
                    telephone: '+54-223-660-2699',
                    contactType: 'customer service',
                    availableLanguage: 'Spanish',
                    areaServed: 'AR',
                  },
                },
                {
                  '@type': 'LocalBusiness',
                  '@id': `${baseUrl}#localbusiness`,
                  name: 'Envíos DosRuedas',
                  description: 'Mensajería y logística e-commerce en Mar del Plata. Envíos Express en franja de 3 hs a elección, LowCost, Mercado Envíos Flex y almacenamiento en Friuli 1972.',
                  url: baseUrl,
                  telephone: '+54-223-660-2699',
                  email: 'matiascejas@enviosdosruedas.com',
                  image: `${baseUrl}/og-image.jpg`,
                  hasMap: 'https://maps.google.com/?q=Friuli+1972,+Mar+del+Plata',
                  address: {
                    '@type': 'PostalAddress',
                    streetAddress: 'Friuli 1972',
                    addressLocality: 'Mar del Plata',
                    addressRegion: 'Buenos Aires',
                    postalCode: '7600',
                    addressCountry: 'AR',
                  },
                  geo: {
                    '@type': 'GeoCoordinates',
                    latitude: -38.0055,
                    longitude: -57.5426,
                  },
                  openingHoursSpecification: [
                    {
                      '@type': 'OpeningHoursSpecification',
                      dayOfWeek: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                      opens: '09:00',
                      closes: '18:00',
                    },
                    {
                      '@type': 'OpeningHoursSpecification',
                      dayOfWeek: ['Saturday'],
                      opens: '10:00',
                      closes: '15:00',
                    },
                  ],
                  areaServed: { '@type': 'City', name: 'Mar del Plata' },
                  priceRange: '$$',
                  currenciesAccepted: 'ARS',
                  paymentAccepted: 'Cash, Credit Card, Transfer, MercadoPago',
                },
              ],
            }, null, 2)
          }}
        />
        <Script src="https://www.googletagmanager.com/gtag/js?id=AW-17510443994" strategy="lazyOnload" />
        <Script id="google-tag-init" strategy="lazyOnload">
          {`
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'AW-17510443994');
            gtag('config', 'G-LSLQ3RJ8WT');
          `}
        </Script>
      </head>
      <body className="bg-brand-white text-brand-ink font-sans antialiased selection:bg-brand-yellow selection:text-brand-blue min-h-dvh flex flex-col" suppressHydrationWarning>
        <MotionConfig reducedMotion="user">
          <ClientLayout>{children}</ClientLayout>
        </MotionConfig>
      </body>
    </html>
  );
}

```

### Client Layout (src/components/ClientLayout.tsx) (`src/components/ClientLayout.tsx`)

```tsx
'use client';

import React, { useEffect } from 'react';
import dynamic from 'next/dynamic';
import OptimizedHeader from './layout/OptimizedHeader';
import OptimizedFooter from './layout/OptimizedFooter';
import { captureAndPersistUtms } from '@/lib/analytics';

// CarruselRedes contains GSAP ScrollTrigger and is dynamically imported to avoid blocking FCP / TBT on initial paint
const CarruselRedes = dynamic(() => import('./layout/CarruselRedes'), {
  loading: () => <div className="w-full py-16 bg-brand-blue-500 min-h-62.5" />,
  ssr: true,
});

export default function ClientLayout({ children }: { children: React.ReactNode }) {
  useEffect(() => {
    captureAndPersistUtms();
  }, []);

  return (
    <>
      <OptimizedHeader />
      <main id="main-content" className="grow pt-18">
        {children}
      </main>
      <CarruselRedes />
      <OptimizedFooter />
    </>
  );
}

```

### Optimized Header (src/components/layout/OptimizedHeader.tsx) (`src/components/layout/OptimizedHeader.tsx`)

```tsx
'use client';

import React, { useState, useEffect, useRef, useMemo, useCallback } from 'react';
import Link from 'next/link';
import Image from 'next/image';
import dynamic from 'next/dynamic';
import { usePathname } from 'next/navigation';
import { AnimatePresence, motion, useReducedMotion, type Variants } from 'motion/react';
import {
  Menu, X, ChevronDown, Bike, ChevronRight, Phone,
  Home, Zap, TrendingDown, Clock, ShoppingBag, Info, HelpCircle, Share2, Mail,
  LayoutGrid, HandCoins, Building2, Rocket, Package, Store
} from 'lucide-react';
import { CTANestedPill } from '@/components/ui/CTANestedPill';

const MobileNav = dynamic(() => import('./MobileNav'), { ssr: false });

interface NavItem {
  label: string;
  href?: string;
  icon?: React.ComponentType<{ className?: string }>;
  dropdownItems?: { label: string; href: string; icon?: React.ComponentType<{ className?: string }> }[];
}

const EASE_MOUNT = { duration: 0.45, ease: [0.25, 0.8, 0.25, 1] } as const;

// NAV ITEMS - Static data, move outside component to avoid recreation on every render
const NAV_ITEMS: NavItem[] = [
  { label: 'Inicio', href: '/', icon: Home },
  {
    label: 'Servicios',
    icon: Bike,
    dropdownItems: [
      { label: 'Todos los Servicios', href: '/servicios', icon: LayoutGrid },
      { label: 'Envíos Express', href: '/servicios/envios-express', icon: Zap },
      { label: 'Envíos LowCost', href: '/servicios/envios-lowcost', icon: TrendingDown },
      { label: 'Envíos Flex (MeLi)', href: '/servicios/enviosflex', icon: Clock },
      { label: 'Cuenta Corriente Flexible', href: '/servicios/empresas-cuenta-corriente', icon: Building2 },
      { label: 'E-commerce 24HS', href: '/servicios#ecommerce-24hs', icon: Package },
      { label: 'E-commerce Same Day', href: '/servicios/deposito-fulfillment', icon: Store },
    ],
  },
  {
    label: 'Nosotros',
    icon: Info,
    dropdownItems: [
      { label: 'Sobre Nosotros', href: '/nosotros/sobre-nosotros', icon: Info },
      { label: 'Preguntas Frecuentes', href: '/nosotros/preguntas-frecuentes', icon: HelpCircle },
      { label: 'Nuestras Redes', href: '/nosotros/nuestras-redes', icon: Share2 },
    ],
  },
  { label: 'Contacto', href: '/contacto', icon: Mail },
];

export default function OptimizedHeader() {
  const [isOpen, setIsOpen] = useState(false);
  const [activeDropdown, setActiveDropdown] = useState<string | null>(null);
  const [scrolled, setScrolled] = useState(false);
  const pathname = usePathname();
  const prefersReducedMotion = useReducedMotion();
  const prevPathRef = useRef(pathname);

  // Memoize dropdown variants to avoid recreation on every render
  const dropdownContainer = useMemo<Variants>(() => ({
    hidden: { opacity: 0, y: prefersReducedMotion ? 0 : 8, scale: prefersReducedMotion ? 1 : 0.97 },
    visible: {
      opacity: 1, y: 0, scale: 1,
      transition: { type: 'spring', stiffness: 320, damping: 24, staggerChildren: prefersReducedMotion ? 0 : 0.06, delayChildren: 0.02 },
    },
    exit: { opacity: 0, y: prefersReducedMotion ? 0 : 6, scale: prefersReducedMotion ? 1 : 0.97, transition: { duration: 0.15, ease: 'easeIn' as const } },
  }), [prefersReducedMotion]);

  const dropdownItem = useMemo<Variants>(() => ({
    hidden: { opacity: 0, x: prefersReducedMotion ? 0 : -8 },
    visible: { opacity: 1, x: 0, transition: { type: 'spring', stiffness: 400, damping: 28 } },
  }), [prefersReducedMotion]);

  const handleDropdownToggle = useCallback((label: string) => {
    setActiveDropdown(prev => (prev === label ? null : label));
  }, []);

  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 20);
    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  // FIX ESLINT react-hooks/set-state-in-effect: cierra drawer al cambiar ruta sin setState sincrónico en effect
  // Usamos ref + async microtask para no ser sincrónico
  useEffect(() => {
    if (prevPathRef.current !== pathname) {
      prevPathRef.current = pathname;
      // Solo si está abierto, lo cerramos en próximo tick (no sincrónico)
      if (isOpen || activeDropdown) {
        const id = setTimeout(() => {
          setIsOpen(false);
          setActiveDropdown(null);
        }, 0);
        return () => clearTimeout(id);
      }
    }
  }, [pathname, isOpen, activeDropdown]);

  // Lock scroll robusto
  useEffect(() => {
    if (isOpen) {
      const scrollY = window.scrollY;
      document.body.style.position = 'fixed';
      document.body.style.top = `-${scrollY}px`;
      document.body.style.width = '100%';
      document.body.style.overflow = 'hidden';
      return () => {
        document.body.style.position = '';
        document.body.style.top = '';
        document.body.style.width = '';
        document.body.style.overflow = '';
        window.scrollTo(0, scrollY);
      };
    }
  }, [isOpen]);

  return (
    <>
      <header
        id="optimized-header"
        className={`fixed top-0 left-0 right-0 z-50 w-full transition-[background-color,border-color,box-shadow,padding] duration-300 ${
          scrolled ? 'bg-brand-blue-700/95 shadow-elevated border-b border-white/10 py-2.5 backdrop-blur-md' : 'bg-brand-blue-700 py-4 border-b border-transparent'
        }`}
      >
        <motion.div initial={prefersReducedMotion ? false : { opacity: 0, y: -8 }} animate={{ opacity: 1, y: 0 }} transition={EASE_MOUNT} className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between">
            <Link href="/" id="nav-logo-opt" className="flex items-center gap-3 group focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-yellow-500 rounded-xl">
              <div className="flex items-center gap-2.5">
                <motion.div className="relative w-10 h-10 shrink-0" whileHover={prefersReducedMotion ? {} : { rotate: 12, scale: 1.08 }} whileTap={prefersReducedMotion ? {} : { scale: 0.95 }} transition={{ type: 'spring', stiffness: 500, damping: 18 }}>
                  {/* `sizes` es obligatorio con `fill`: sin él Next asume 100vw y el browser
    descarga la variante de 1536px para una caja de 40x40. Medido en producción:
    25.598 bytes de los cuales 25.534 eran desperdicio (99,7%). Como lleva
    `priority`, se precarga en el critical path de todas las páginas. */}
<Image
  src="/logo-envios-simplified.webp"
  alt="Logo Envíos Dos Ruedas"
  fill
  sizes="40px"
  className="object-contain"
  priority
/>
                </motion.div>
                <span className="font-display text-2xl sm:text-3xl tracking-tight leading-none uppercase select-none flex flex-col sm:flex-row sm:gap-1 items-start sm:items-center">
                  <span className="text-white kinetic-font-stretch">Envíos</span>
                  <span className="text-brand-yellow-500 kinetic-font-stretch">DosRuedas</span>
                </span>
              </div>
            </Link>

            <nav id="desktop-nav-opt" className="hidden lg:flex items-center gap-2">
              {NAV_ITEMS.map((item) => (
                <div key={item.label} className="relative" onMouseEnter={() => item.dropdownItems && setActiveDropdown(item.label)} onMouseLeave={() => setActiveDropdown(null)}>
                  {item.href ? (
                    <Link href={item.href} className="px-4 py-2.5 rounded-xl text-base font-subheading font-bold uppercase tracking-wider text-white hover:text-brand-yellow-500 hover:bg-white/10 transition-colors">{item.label}</Link>
                  ) : (
                    <button onClick={() => handleDropdownToggle(item.label)} aria-haspopup="menu" aria-expanded={activeDropdown === item.label} className="px-4 py-2.5 rounded-xl text-base font-subheading font-bold uppercase tracking-wider text-white hover:text-brand-yellow-500 hover:bg-white/10 transition-colors flex items-center gap-1.5">
                      {item.label}<ChevronDown className={`h-4 w-4 transition-transform ${activeDropdown === item.label ? 'rotate-180' : ''}`} />
                    </button>
                  )}
                  <AnimatePresence>
                    {item.dropdownItems && activeDropdown === item.label && (
                      <motion.div variants={dropdownContainer} initial="hidden" animate="visible" exit="exit" className="absolute left-0 mt-2 w-64 bg-brand-blue-700 rounded-2xl shadow-2xl border border-white/15 py-2.5 text-white overflow-hidden z-50">
                        <div className="flex flex-col gap-1 px-2">
                          {item.dropdownItems.map((subItem) => {
                            const SubIcon = subItem.icon || ChevronRight;
                            return (
                              <motion.div key={subItem.href} variants={dropdownItem}>
                                <Link href={subItem.href} className="flex items-center gap-3 px-3 py-2.5 rounded-xl transition-colors hover:bg-white/10 text-white hover:text-brand-yellow-500 group focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-yellow-500">
                                  <div className="p-1.5 rounded-lg bg-white/10 text-brand-blue-50 group-hover:bg-brand-yellow-500 group-hover:text-brand-blue-700 transition-colors shrink-0"><SubIcon className="h-4 w-4" /></div>
                                  <span className="text-base font-bold uppercase font-subheading tracking-wider leading-none">{subItem.label}</span>
                                </Link>
                              </motion.div>
                            );
                          })}
                        </div>
                      </motion.div>
                    )}
                  </AnimatePresence>
                </div>
              ))}
            </nav>

            <div className="hidden lg:flex items-center gap-5">
              <a href="tel:+542236602699" className="flex items-center gap-2 text-white hover:text-brand-yellow-500 transition-colors font-mono text-base font-bold"><Phone className="h-4 w-4 text-brand-yellow-500" /><span>223 660-2699</span></a>
              <div className="relative">
                {!(pathname === '/' || pathname.startsWith('/servicios') || pathname.startsWith('/cotizar')) && !prefersReducedMotion && (
                  <motion.span className="absolute inset-0 rounded-full bg-brand-yellow-500/25 pointer-events-none" animate={{ scale: [1, 1.18, 1], opacity: [0.6, 0, 0.6] }} transition={{ duration: 2.4, repeat: Infinity, ease: 'easeInOut', repeatDelay: 1.5 }} />
                )}
                <CTANestedPill href="/cotizar" variant={(pathname === '/' || pathname.startsWith('/servicios') || pathname.startsWith('/cotizar')) ? 'outline' : 'primary'} size="default" className={(pathname === '/' || pathname.startsWith('/servicios') || pathname.startsWith('/cotizar')) ? 'border-white/40 text-white hover:bg-white/10 hover:border-white' : ''}>Cotizá tu envío</CTANestedPill>
              </div>
            </div>

            <div className="lg:hidden flex items-center gap-3">
              <a href="tel:+542236602699" className="p-2.5 rounded-xl bg-white/10 hover:bg-white/15 text-white hover:text-brand-yellow-500 focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-yellow-500 transition-all min-w-11 min-h-11 flex items-center justify-center" aria-label="Llamar"><Phone className="h-5 w-5 text-brand-yellow-500" /></a>
              <button onClick={() => setIsOpen(!isOpen)} id="mobile-menu-toggle-opt" className="p-2.5 rounded-xl bg-white/10 hover:bg-white/15 text-white hover:text-brand-yellow-500 focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-yellow-500 transition-all cursor-pointer min-w-11 min-h-11 flex items-center justify-center" aria-label={isOpen ? 'Cerrar menú' : 'Abrir menú'} aria-expanded={isOpen} aria-controls="mobile-navigation-dialog">
                <AnimatePresence mode="wait" initial={false}>
                  {isOpen ? (
                    <motion.span key="close" initial={prefersReducedMotion ? false : { rotate: -90, opacity: 0 }} animate={{ rotate: 0, opacity: 1 }} exit={prefersReducedMotion ? {} : { rotate: 90, opacity: 0 }} transition={{ duration: 0.18 }}><X className="h-6 w-6" /></motion.span>
                  ) : (
                    <motion.span key="menu" initial={prefersReducedMotion ? false : { rotate: 90, opacity: 0 }} animate={{ rotate: 0, opacity: 1 }} exit={prefersReducedMotion ? {} : { rotate: -90, opacity: 0 }} transition={{ duration: 0.18 }}><Menu className="h-6 w-6" /></motion.span>
                  )}
                </AnimatePresence>
              </button>
            </div>
          </div>
        </motion.div>
      </header>

      <AnimatePresence>{isOpen && <MobileNav isOpen={isOpen} onClose={() => setIsOpen(false)} navItems={NAV_ITEMS} activeDropdown={activeDropdown} onDropdownToggle={handleDropdownToggle} />}</AnimatePresence>
    </>
  );
}

```

### Mobile Navigation Drawer (src/components/layout/MobileNav.tsx) (`src/components/layout/MobileNav.tsx`)

```tsx
'use client';

import React, { useEffect } from 'react';
import Link from 'next/link';
import { createPortal } from 'react-dom';
import { motion, AnimatePresence, useReducedMotion } from 'motion/react';
import { ChevronDown, ChevronRight, Phone, X } from 'lucide-react';
import { CTANestedPill } from '@/components/ui';

export interface MobileNavItem {
  label: string;
  href?: string;
  icon?: React.ComponentType<{ className?: string }>;
  dropdownItems?: { label: string; href: string; icon?: React.ComponentType<{ className?: string }> }[];
}

export interface MobileNavProps {
  isOpen: boolean;
  onClose: () => void;
  navItems: MobileNavItem[];
  activeDropdown: string | null;
  onDropdownToggle: (label: string) => void;
}

const SPRING_PANEL = { type: 'spring', stiffness: 340, damping: 30 } as const;
const NAV_CONTAINER = { hidden: {}, visible: { transition: { staggerChildren: 0.07, delayChildren: 0.15 } } } as const;
const NAV_ITEM_VARIANT = { hidden: { opacity: 0, x: 24 }, visible: { opacity: 1, x: 0, transition: { type: 'spring', stiffness: 380, damping: 26 } } } as const;

// FIX ESLINT: useSyncExternalStore para mounted sin setState en effect
function useIsMounted() {
  return React.useSyncExternalStore(
    () => () => {},
    () => true,
    () => false
  );
}

export const MobileNav: React.FC<MobileNavProps> = ({ isOpen, onClose, navItems, activeDropdown, onDropdownToggle }) => {
  const prefersReducedMotion = useReducedMotion();
  const mounted = useIsMounted();
  const drawerRef = React.useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!isOpen) return;
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        e.preventDefault();
        onClose();
        return;
      }
      if (e.key === 'Tab' && drawerRef.current) {
        const focusable = drawerRef.current.querySelectorAll<HTMLElement>('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
        if (focusable.length === 0) return;
        const first = focusable[0];
        const last = focusable[focusable.length - 1];
        if (e.shiftKey && document.activeElement === first) {
          e.preventDefault();
          last.focus();
        } else if (!e.shiftKey && document.activeElement === last) {
          e.preventDefault();
          first.focus();
        }
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    const t = setTimeout(() => drawerRef.current?.querySelector<HTMLElement>('button, [href]')?.focus(), 80);
    return () => {
      window.removeEventListener('keydown', handleKeyDown);
      clearTimeout(t);
      document.getElementById('mobile-menu-toggle-opt')?.focus();
    };
  }, [isOpen, onClose]);

  if (!mounted) return null;

  const content = (
    <>
      <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} transition={{ duration: prefersReducedMotion ? 0 : 0.2 }} onClick={onClose} className="fixed inset-0 bg-brand-blue-700/70 backdrop-blur-md z-99 lg:hidden" />
      <motion.div
        ref={drawerRef}
        id="mobile-navigation-dialog"
        role="dialog"
        aria-modal="true"
        aria-label="Menú principal"
        initial={prefersReducedMotion ? { x: 0 } : { x: '100%' }}
        animate={{ x: 0 }}
        exit={prefersReducedMotion ? { opacity: 0 } : { x: '100%' }}
        transition={SPRING_PANEL}
        className="fixed top-0 right-0 bottom-0 z-100 flex flex-col w-full max-w-[320px] h-dvh bg-brand-blue-700 shadow-2xl border-l border-white/10 lg:hidden overscroll-contain"
      >
        <div className="flex items-center justify-between px-5 py-4 border-b border-white/10 shrink-0 h-16">
          <Link href="/" onClick={onClose} className="flex items-center gap-3 focus:outline-none focus:ring-2 focus:ring-brand-yellow-500/50 rounded-lg">
            <span className="font-display text-xl tracking-tight uppercase select-none flex flex-col items-start leading-none">
              <span className="text-white">Envíos</span>
              <span className="text-brand-yellow-500">DosRuedas</span>
            </span>
          </Link>
          <motion.button onClick={onClose} whileHover={prefersReducedMotion ? {} : { scale: 1.08, rotate: 90 }} whileTap={prefersReducedMotion ? {} : { scale: 0.92 }} transition={{ type: 'spring', stiffness: 500, damping: 20 }} className="p-2.5 rounded-xl bg-white/10 hover:bg-white/15 text-white hover:text-brand-yellow-500 focus:outline-none focus:ring-2 focus:ring-brand-yellow-500/50 transition-colors cursor-pointer min-w-11 min-h-11 flex items-center justify-center" aria-label="Cerrar menú">
            <X className="h-5 w-5" />
          </motion.button>
        </div>

        <div className="flex-1 overflow-y-auto overscroll-contain px-5 py-6 space-y-6">
          <motion.nav className="space-y-2" variants={prefersReducedMotion ? {} : NAV_CONTAINER} initial="hidden" animate="visible">
            {navItems.map((item) => (
              <motion.div key={item.label} variants={prefersReducedMotion ? {} : NAV_ITEM_VARIANT} className="border-b border-white/10 pb-2.5 last:border-b-0 last:pb-0">
                {item.href ? (
                  <Link href={item.href} onClick={onClose} className="flex items-center gap-3.5 py-2.5 px-3 rounded-xl text-xl font-subheading tracking-wider uppercase text-white hover:text-brand-yellow-500 hover:bg-white/5 transition-all font-bold min-h-12 focus:outline-none focus:ring-2 focus:ring-brand-yellow-500/50">
                    {item.icon && <item.icon className="h-5 w-5 text-brand-yellow-500 shrink-0" />}
                    <span>{item.label}</span>
                  </Link>
                ) : (
                  <div>
                    <button onClick={() => onDropdownToggle(item.label)} className="w-full text-left py-2.5 px-3 rounded-xl text-xl font-subheading tracking-wider uppercase flex items-center justify-between text-white hover:bg-white/5 font-bold cursor-pointer transition-all min-h-12 focus:outline-none focus:ring-2 focus:ring-brand-yellow-500/50">
                      <span className="flex items-center gap-3.5">{item.icon && <item.icon className="h-5 w-5 text-brand-yellow-500 shrink-0" />}<span>{item.label}</span></span>
                      <motion.span animate={{ rotate: activeDropdown === item.label ? 180 : 0 }} transition={{ type: 'spring', stiffness: 400, damping: 25 }}><ChevronDown className="h-5 w-5 text-brand-yellow-500 shrink-0" /></motion.span>
                    </button>
                    <AnimatePresence>
                      {item.dropdownItems && activeDropdown === item.label && (
                        <motion.div initial={{ opacity: 0, height: 0 }} animate={{ opacity: 1, height: 'auto' }} exit={{ opacity: 0, height: 0 }} transition={prefersReducedMotion ? { duration: 0 } : { type: 'spring', stiffness: 340, damping: 28 }} className="pl-4 pr-1 py-2 flex flex-col gap-1 overflow-hidden">
                          {item.dropdownItems.map((subItem, idx) => {
                            const SubIcon = subItem.icon || ChevronRight;
                            return (
                              <motion.div key={subItem.href} initial={prefersReducedMotion ? {} : { opacity: 0, x: 12 }} animate={{ opacity: 1, x: 0 }} transition={{ delay: idx * 0.05, type: 'spring', stiffness: 380, damping: 26 }}>
                                <Link href={subItem.href} onClick={onClose} className="flex items-center gap-3 py-2 px-3 rounded-xl text-base font-subheading uppercase tracking-wider font-bold text-brand-blue-50/90 hover:text-brand-yellow-500 hover:bg-white/10 transition-all min-h-10.5 focus:outline-none focus:ring-2 focus:ring-brand-yellow-500/50">
                                  <div className="p-1 rounded-lg bg-white/10 text-brand-yellow-500 shrink-0"><SubIcon className="h-4 w-4" /></div><span>{subItem.label}</span>
                                </Link>
                              </motion.div>
                            );
                          })}
                        </motion.div>
                      )}
                    </AnimatePresence>
                  </div>
                )}
              </motion.div>
            ))}
          </motion.nav>
        </div>

        <div className="p-5 border-t border-white/10 space-y-4 shrink-0 bg-brand-blue-700 backdrop-blur-md mt-auto">
          <a href="tel:+542236602699" className="flex items-center justify-center gap-2.5 py-3 px-4 rounded-xl bg-white/10 border border-white/5 text-white hover:text-brand-yellow-500 font-mono text-sm font-bold transition-all min-h-11 focus:outline-none focus:ring-2 focus:ring-brand-yellow-500/50"><Phone className="h-4 w-4 text-brand-yellow-500" /><span>+54 223 660-2699</span></a>
          <CTANestedPill href="/cotizar" variant="primary" size="large" className="w-full justify-center min-h-11 py-3.5" onClick={onClose}>Cotizá tu envío</CTANestedPill>
        </div>
      </motion.div>
    </>
  );

  return createPortal(content, document.body);
};

export default MobileNav;

```

### Carrusel Redes (src/components/layout/CarruselRedes.tsx) (`src/components/layout/CarruselRedes.tsx`)

```tsx
'use client';

import React, { useEffect, useRef } from 'react';
import { FaInstagram, FaFacebook, FaWhatsapp } from 'react-icons/fa';
import { ArrowUpRight } from 'lucide-react';
import { useReducedMotion } from 'motion/react';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

export default function CarruselRedes() {
  const sectionRef = useRef<HTMLDivElement>(null);
  const containerRef = useRef<HTMLDivElement>(null);
  const prefersReducedMotion = useReducedMotion();

  useEffect(() => {
    gsap.registerPlugin(ScrollTrigger);

    // Early return for reduced motion - no animations at all
    if (prefersReducedMotion) {
      // Ensure blocks are visible without animation
      if (containerRef.current) {
        const blocks = containerRef.current.querySelectorAll('.social-block');
        blocks.forEach((block) => {
          (block as HTMLElement).style.opacity = '1';
          (block as HTMLElement).style.transform = 'none';
        });
      }
      return;
    }

    const ctx = gsap.context(() => {
      if (containerRef.current) {
        const blocks = containerRef.current.querySelectorAll('.social-block');
        gsap.fromTo(
          blocks,
          {
            y: 50,
            opacity: 0,
            scale: 0.96,
          },
          {
            y: 0,
            opacity: 1,
            scale: 1,
            stagger: 0.15,
            duration: 0.8,
            ease: 'power3.out',
            scrollTrigger: {
              trigger: containerRef.current,
              start: 'top 85%',
              once: true,
            },
          }
        );
      }
    }, sectionRef);

    return () => ctx.revert();
  }, [prefersReducedMotion]);

  const networks = [
    {
      id: 'facebook',
      name: 'FACEBOOK',
      handle: 'Envíos DosRuedas',
      desc: 'Seguí nuestro día a día, novedades operativas y la comunidad comercial en Mar del Plata.',
      action: 'SEGUIR COMUNIDAD',
      url: 'https://www.facebook.com/share/1RnSzyweir/',
      icon: FaFacebook,
      badgeText: 'FACEBOOK OFICIAL',
      // Estética propia Facebook (Royal Classic Blue)
      cardBg: 'bg-[#1877F2]/10 hover:bg-[#1877F2]/15',
      cardBorder: 'border-[#1877F2]/30 hover:border-[#1877F2]/70',
      badgeBg: 'bg-[#1877F2]/20 text-brand-blue-50 border-[#1877F2]/40',
      iconBoxBg: 'bg-[#0B5ED7] text-white shadow-lg shadow-[#1877F2]/40',
      handleColor: 'text-brand-blue-50',
      watermarkColor: 'text-[#1877F2]/10 group-hover:text-[#1877F2]/20',
      btnBg: 'bg-[#0B5ED7] hover:bg-[#0A4FC0] text-white shadow-md shadow-[#1877F2]/30',
      btnIconBg: 'bg-white/20 text-white',
      glow: 'from-[#1877F2]/20 to-transparent',
    },
    {
      id: 'instagram',
      name: 'INSTAGRAM',
      handle: '@enviosdosruedas',
      desc: 'Mirá el detrás de escena de nuestros riders y la flota recorriendo las calles de MDQ.',
      action: 'VER CONTENIDO',
      url: 'https://www.instagram.com/enviosdosruedas/',
      icon: FaInstagram,
      badgeText: 'INSTAGRAM MDQ',
      // Estética propia Instagram (Gradient Sunset & Pink/Purple)
      cardBg: 'bg-gradient-to-br from-[#833AB4]/10 via-[#FD1D1D]/10 to-[#F77737]/10 hover:from-[#833AB4]/15 hover:via-[#FD1D1D]/15 hover:to-[#F77737]/15',
      cardBorder: 'border-[#E1306C]/30 hover:border-[#E1306C]/70',
      badgeBg: 'bg-linear-to-r from-[#833AB4]/20 via-[#FD1D1D]/20 to-[#F77737]/20 text-brand-blue-50 border-[#E1306C]/40',
      iconBoxBg: 'bg-linear-to-tr from-[#F56040] via-[#FD1D1D] to-[#833AB4] text-white shadow-lg shadow-[#E1306C]/40',
      handleColor: 'text-brand-blue-50',
      watermarkColor: 'text-[#E1306C]/10 group-hover:text-[#E1306C]/20',
      btnBg: 'bg-linear-to-r from-[#833AB4] via-[#FD1D1D] to-[#F77737] hover:opacity-95 text-white shadow-md shadow-[#FD1D1D]/30',
      btnIconBg: 'bg-white/20 text-white',
      glow: 'from-[#E1306C]/20 to-transparent',
    },
    {
      id: 'whatsapp',
      name: 'WHATSAPP',
      handle: '+54 223 660-2699',
      desc: 'Escribinos directamente para consultas, contrataciones o soporte express al toque.',
      action: 'INICIAR CHAT',
      url: 'https://wa.me/542236602699',
      icon: FaWhatsapp,
      badgeText: 'WHATSAPP DIRECTO',
      // Estética oficial Envíos DosRuedas (Brand Yellow & Navy Blue)
      cardBg: 'bg-brand-yellow-500/10 hover:bg-brand-yellow-500/15',
      cardBorder: 'border-brand-yellow-500/30 hover:border-brand-yellow-500/70',
      badgeBg: 'bg-brand-yellow-500/20 text-brand-yellow-500 border-brand-yellow-500/40',
      iconBoxBg: 'bg-brand-yellow-500 text-brand-blue-900 shadow-lg shadow-brand-yellow-500/30',
      handleColor: 'text-brand-yellow-400',
      watermarkColor: 'text-brand-yellow-500/10 group-hover:text-brand-yellow-500/20',
      btnBg: 'bg-brand-yellow-500 hover:bg-brand-yellow-400 text-brand-blue-900 font-bold shadow-md shadow-brand-yellow-500/30',
      btnIconBg: 'bg-transparent text-brand-blue-900',
      glow: 'from-brand-yellow-500/20 to-transparent',
    },
  ];

  return (
    <section
      ref={sectionRef}
      id="carrusel-redes"
      suppressHydrationWarning
      className="py-20 md:py-32 bg-brand-blue border-y border-white/10 relative overflow-hidden font-sans select-none"
    >
      {/* Background Decorative Mesh & Depth Highlights */}
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_0%,rgba(255,236,1,0.08),transparent_50%)] pointer-events-none" />
      <div className="absolute top-0 left-1/4 w-100 h-100 bg-brand-blue-500/10 rounded-full blur-[100px] pointer-events-none" />

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        
        {/* Header Segment */}
        <div className="text-center max-w-3xl mx-auto mb-16 space-y-4">
          <span className="px-4 py-1.5 bg-brand-yellow-500 text-brand-blue-900 rounded-full text-xs font-bold tracking-widest inline-block font-subheading uppercase shadow-accent-sm">
            Nuestra Comunidad Digital
          </span>
          
          <h2 className="text-white text-4xl sm:text-5xl lg:text-6xl font-display uppercase tracking-tight leading-[0.95] text-center">
            SEGUÍ NUESTRO <span className="text-brand-yellow-500">MOVIMIENTO</span>
          </h2>

          <p className="text-brand-blue-50 text-sm sm:text-base leading-relaxed font-sans max-w-2xl mx-auto opacity-90">
            Sumate a nuestros canales digitales y enterate al toque de todas las novedades operativas en Mar del Plata.
          </p>
          <div className="h-0.5 w-20 bg-brand-yellow-500 mx-auto rounded-full mt-4" />
        </div>

        {/* Networks Grid: 3 Unique Branded Cards */}
        <div
          ref={containerRef}
          className="grid grid-cols-1 md:grid-cols-3 gap-6 lg:gap-8 w-full"
        >
          {networks.map((net) => {
            const Icon = net.icon;

            return (
              <div
                key={net.id}
                className={`social-block group relative rounded-2xl p-2 transition-[transform,border-color,box-shadow] duration-300 border ${net.cardBorder} bg-brand-blue/80 backdrop-blur-md hover:-translate-y-1.5 shadow-xl`}
              >
                {/* Internal Glow on Hover */}
                <div className={`absolute inset-0 rounded-2xl bg-linear-to-b ${net.glow} opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none`} />

                <div className={`relative rounded-xl p-6 sm:p-7 flex flex-col justify-between h-97.5 md:h-107.5 overflow-hidden ${net.cardBg} border border-white/10 transition-colors`}>
                  
                  {/* Background Watermark Icon that enlarges and tilts on hover */}
                  <div className={`absolute -right-8 -bottom-8 ${net.watermarkColor} transition-transform duration-500 ease-out group-hover:scale-125 group-hover:-rotate-12 pointer-events-none select-none`}>
                    <Icon className="w-56 h-56" />
                  </div>

                  {/* Top Area: Badge & Branded Icon Box */}
                  <div className="z-10 text-left space-y-4">
                    <div className="flex items-center justify-between">
                      <span className={`text-2xs font-bold tracking-widest px-3 py-1 rounded-full uppercase font-subheading border ${net.badgeBg}`}>
                        {net.badgeText}
                      </span>

                      <div className={`w-11 h-11 rounded-xl flex items-center justify-center transition-transform duration-300 group-hover:scale-110 ${net.iconBoxBg}`}>
                        <Icon className="w-5 h-5" />
                      </div>
                    </div>

                    <div>
                      <h3 className="font-display text-3xl sm:text-4xl uppercase tracking-tight leading-none text-white">
                        {net.name}
                      </h3>
                      <p className={`font-mono text-xs font-bold mt-1.5 ${net.handleColor}`}>
                        {net.handle}
                      </p>
                    </div>

                    <p className="font-sans text-xs sm:text-sm leading-relaxed text-brand-blue-50/90 font-light">
                      {net.desc}
                    </p>
                  </div>

                  {/* Bottom Action Area: Custom CTA Button per Network */}
                  <div className="z-10 pt-4 border-t border-white/10">
                    <a
                      href={net.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className={`w-full inline-flex items-center justify-between font-subheading font-bold uppercase tracking-wider text-xs sm:text-sm px-5 py-3 rounded-full transition-colors duration-200 group/btn ${net.btnBg}`}
                    >
                      <span>{net.action}</span>
                      <span className={`w-7 h-7 rounded-full flex items-center justify-center shrink-0 ml-2 transition-transform duration-200 group-hover/btn:translate-x-1 ${net.btnIconBg}`}>
                        <ArrowUpRight className="w-4 h-4" />
                      </span>
                    </a>
                  </div>

                </div>
              </div>
            );
          })}
        </div>

      </div>
    </section>
  );
}


```

### Optimized Footer (src/components/layout/OptimizedFooter.tsx) (`src/components/layout/OptimizedFooter.tsx`)

```tsx
'use client';

import React from 'react';
import Link from 'next/link';
import Image from 'next/image';
import { motion, useReducedMotion } from 'motion/react';
import {
  Phone, MapPin, Mail, Clock, ShieldCheck, ArrowUpRight,
  Zap, TrendingDown, ShoppingBag, ArrowUp, Rocket, Layers, Building2, Package, Store
} from 'lucide-react';
import { FaInstagram, FaFacebook, FaWhatsapp } from 'react-icons/fa';

// ─── Animation Variants ───────────────────────────────────────────────────────

/** Fade-up stagger container for footer columns */
const FOOTER_CONTAINER = {
  hidden: {},
  visible: {
    transition: { staggerChildren: 0.12, delayChildren: 0.1 },
  },
} as const;

/** Each column fades up */
const FOOTER_COL = {
  hidden: { opacity: 0, y: 28 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { type: 'spring', stiffness: 280, damping: 24 },
  },
} as const;

/** CTA Banner slides up from below */
const BANNER_VARIANT = {
  hidden: { opacity: 0, y: 40 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { type: 'spring', stiffness: 260, damping: 22, delay: 0.08 },
  },
} as const;

/** Social icon spring bounce on hover */
const SOCIAL_HOVER = { y: -4, scale: 1.12 } as const;
const SOCIAL_SPRING = { type: 'spring', stiffness: 480, damping: 18 } as const;

export default function OptimizedFooter() {
  const prefersReducedMotion = useReducedMotion();

  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <footer
      id="optimized-footer"
      className="bg-brand-blue-700 text-white border-t border-white/10 relative overflow-hidden font-sans select-none"
    >
      {/* Decorative top yellow accent bar with continuous glow */}
      <div className="h-1.5 bg-brand-yellow-500 w-full shadow-md shadow-brand-yellow-500/30" />

      {/* Atmospheric Background & Subtle Blueprint Grid Details */}
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_0%,rgba(255,236,1,0.08),transparent_50%)] pointer-events-none" />
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_10%_90%,rgba(9,80,246,0.5),transparent_40%)] pointer-events-none" />
      <div className="absolute inset-0 opacity-5 bg-[linear-gradient(to_right,#ffffff_1px,transparent_1px),linear-gradient(to_bottom,#ffffff_1px,transparent_1px)] bg-size-[32px_32px] pointer-events-none" />

      {/* Main Container */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-16 pb-12 relative z-10">

        {/* TOP CTA BANNER — slides up from below on scroll reveal */}
        <motion.div
          variants={prefersReducedMotion ? {} : BANNER_VARIANT}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, margin: '-60px' }}
          className="mb-14 rounded-2xl bg-brand-blue/90 border border-white/15 p-6 sm:p-8 backdrop-blur-md shadow-2xl flex flex-col md:flex-row items-center justify-between gap-6"
        >
          <div className="space-y-2 text-center md:text-left">
            <div className="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-brand-yellow-500/15 border border-brand-yellow-500/30 text-brand-yellow-500 text-xs font-subheading font-bold uppercase tracking-wider">
              <span className="w-2 h-2 rounded-full bg-brand-yellow-500 animate-ping motion-reduce:animate-none" />
              Operaciones Activas Mar del Plata 2026
            </div>
            <h3 className="text-2xl sm:text-3xl font-display uppercase tracking-tight text-white">
              ¿Tenés envíos para hoy? <span className="text-brand-yellow-500">Los entregamos a tiempo.</span>
            </h3>
            <p className="text-sm text-brand-blue-50 font-light max-w-xl">
              Cotizá online en segundos o coordiná directo con nuestro equipo logístico por WhatsApp.
            </p>
          </div>

          <div className="flex flex-col sm:flex-row items-center gap-3 w-full md:w-auto shrink-0">
            <Link
              href="/cotizar"
              className="w-full sm:w-auto cta-nested-pill bg-brand-yellow-500 hover:bg-brand-yellow-400 text-brand-blue-900 font-subheading font-bold uppercase tracking-wider text-sm px-6 py-3.5 rounded-full shadow-accent-sm hover:shadow-cta-glow transition-all flex items-center justify-between group min-h-12"
            >
              <span>Cotizá tu Envío</span>
              <span className="cta-nested-icon bg-brand-blue-900/10 text-brand-blue-900 h-7 w-7 rounded-full flex items-center justify-center shrink-0 ml-3 group-hover:translate-x-1 transition-transform">
                <ArrowUpRight className="h-4 w-4" />
              </span>
            </Link>

            <a
              href="https://wa.me/542236602699?text=Hola%20Envíos%20DosRuedas!%20Quiero%20hacer%20una%20consulta%20de%20envíos"
              target="_blank"
              rel="noopener noreferrer"
              aria-label="Chateá con Nosotros por WhatsApp para consultas de envíos"
              className="w-full sm:w-auto inline-flex items-center justify-center gap-2 bg-white/10 hover:bg-white/20 text-white border border-white/20 hover:border-white/40 font-subheading font-bold uppercase tracking-wider text-sm px-5 py-3.5 rounded-full transition-all min-h-12"
            >
              <FaWhatsapp className="h-4 w-4 text-brand-yellow-500" />
              <span>Chateá con Nosotros</span>
            </a>
          </div>
        </motion.div>

        {/* MID SECTION: fade-up stagger per column on scroll reveal */}
        <motion.div
          className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-12 gap-10 lg:gap-12 items-start"
          variants={prefersReducedMotion ? {} : FOOTER_CONTAINER}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, margin: '-60px' }}
        >

          {/* COLUMN 1: Brand details & Socials (4 Cols) */}
          <motion.div
            variants={prefersReducedMotion ? {} : FOOTER_COL}
            className="lg:col-span-4 space-y-6"
          >
            <Link href="/" className="flex items-center gap-3.5 group w-fit focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-yellow-500 rounded-xl">
              <div className="relative w-11 h-11 bg-white/10 p-1.5 rounded-xl border border-white/15 group-hover:scale-105 transition-all duration-300 shrink-0 flex items-center justify-center">
                <Image
                  src="/logo-envios-simplified.webp"
                  alt="Logo Envíos DosRuedas"
                  width={32}
                  height={32}
                  className="object-contain"
                />
              </div>
              <div className="flex flex-col leading-none">
                <span className="font-display text-2xl sm:text-3xl tracking-tight uppercase select-none text-white">
                  Envíos <span className="text-brand-yellow-500">DosRuedas</span>
                </span>
                <span className="text-2xs font-mono text-brand-blue-50 tracking-widest uppercase mt-0.5 opacity-90">
                  Tu solución confiable · Mar del Plata
                </span>
              </div>
            </Link>

            <p className="text-brand-blue-50 text-sm leading-relaxed max-w-sm font-light">
              Con más de 7 años de trayectoria en Mar del Plata, transformamos el despacho de tus productos en un motor de crecimiento para emprendedores, PyMEs y comercios locales con flota propia y compromiso humano.
            </p>

            <div className="space-y-3 pt-2">
              <span className="block text-xs font-bold text-brand-yellow-500 uppercase tracking-widest font-subheading">
                Canales Oficiales
              </span>
              <div className="flex flex-wrap items-center gap-3">
                {/* Instagram — spring bounce */}
                <motion.div
                  whileHover={prefersReducedMotion ? {} : SOCIAL_HOVER}
                  transition={SOCIAL_SPRING}
                  className="inline-block"
                >
                  <Link
                    href="/nosotros/nuestras-redes"
                    className="h-10 w-10 rounded-xl bg-white/10 hover:bg-brand-yellow-500 text-white hover:text-brand-blue-900 flex items-center justify-center transition-colors duration-200 border border-white/15 hover:border-brand-yellow-500 shadow-sm p-2.5 group cursor-pointer"
                    title="Instagram @enviosdosruedas"
                    aria-label="Instagram Oficial"
                  >
                    <FaInstagram className="h-5 w-5" />
                  </Link>
                </motion.div>

                {/* Facebook — spring bounce */}
                <motion.div
                  whileHover={prefersReducedMotion ? {} : SOCIAL_HOVER}
                  transition={SOCIAL_SPRING}
                  className="inline-block"
                >
                  <Link
                    href="/nosotros/nuestras-redes"
                    className="h-10 w-10 rounded-xl bg-white/10 hover:bg-brand-yellow-500 text-white hover:text-brand-blue-900 flex items-center justify-center transition-colors duration-200 border border-white/15 hover:border-brand-yellow-500 shadow-sm p-2.5 group cursor-pointer"
                    title="Facebook Envíos DosRuedas"
                    aria-label="Facebook Oficial"
                  >
                    <FaFacebook className="h-5 w-5" />
                  </Link>
                </motion.div>

                {/* WhatsApp — spring bounce */}
                <motion.div
                  whileHover={prefersReducedMotion ? {} : SOCIAL_HOVER}
                  transition={SOCIAL_SPRING}
                  className="inline-block"
                >
                  <a
                    href="https://wa.me/542236602699"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="h-10 w-10 rounded-xl bg-brand-yellow-500 hover:bg-brand-yellow-400 text-brand-blue-900 flex items-center justify-center transition-colors duration-200 border border-brand-yellow-500 hover:border-brand-yellow-400 shadow-accent-sm hover:shadow-cta-glow p-2.5 group cursor-pointer"
                    title="WhatsApp Directo"
                    aria-label="WhatsApp Directo"
                  >
                    <FaWhatsapp className="h-5 w-5" />
                  </a>
                </motion.div>

                <div className="flex items-center gap-2 px-3.5 py-2 rounded-xl bg-white/10 border border-white/15 text-xs text-white font-mono shadow-inner">
                  <ShieldCheck className="h-4 w-4 text-brand-yellow-500 shrink-0" />
                  <span>Centro de Depósito y Logística Local · Friuli 1972</span>
                </div>
              </div>
            </div>
          </motion.div>

          {/* COLUMN 2: Services & Tools */}
          <motion.div
            variants={prefersReducedMotion ? {} : FOOTER_COL}
            className="lg:col-span-4 space-y-5"
          >
            <h4 className="font-subheading text-lg tracking-wider text-brand-yellow-500 uppercase border-b border-white/10 pb-2 font-bold flex items-center gap-2">
              <span>Servicios y Cotizadores</span>
            </h4>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-x-6 gap-y-4">
              {/* Grupo Cotizadores */}
              <div>
                <p className="text-2xs font-bold text-brand-blue-50/70 uppercase tracking-widest font-subheading mb-2.5">
                  Cotizador online
                </p>
                <ul className="space-y-2.5 text-sm font-sans">
                  <li>
                    <Link
                      href="/cotizar"
                      className="text-brand-blue-50 hover:text-brand-yellow-500 flex items-center justify-between group transition-all duration-200 hover:translate-x-1"
                    >
                      <div className="flex items-center gap-2.5">
                        <Zap className="h-4 w-4 text-brand-yellow-500 shrink-0" />
                        <span>Cotizá Express o LowCost</span>
                      </div>
                      <ArrowUpRight className="h-3.5 w-3.5 opacity-0 group-hover:opacity-100 transition-opacity text-brand-yellow-500" />
                    </Link>
                  </li>
                </ul>
              </div>

              {/* Grupo Servicios y Planes */}
              <div>
                <p className="text-2xs font-bold text-brand-blue-50/70 uppercase tracking-widest font-subheading mb-2.5">
                  Servicios y planes
                </p>
                <ul className="space-y-2.5 text-sm font-sans">
                  <li>
                    <Link
                      href="/servicios/envios-express"
                      className="text-brand-blue-50 hover:text-brand-yellow-500 flex items-center gap-2.5 transition-all duration-200 hover:translate-x-1"
                    >
                      <Zap className="h-4 w-4 text-brand-yellow-500 shrink-0" />
                      <span>Envíos Express</span>
                    </Link>
                  </li>
                  <li>
                    <Link
                      href="/servicios/envios-lowcost"
                      className="text-brand-blue-50 hover:text-brand-yellow-500 flex items-center gap-2.5 transition-all duration-200 hover:translate-x-1"
                    >
                      <TrendingDown className="h-4 w-4 text-brand-yellow-500 shrink-0" />
                      <span>Envíos LowCost</span>
                    </Link>
                  </li>
                  <li>
                    <Link
                      href="/servicios/enviosflex"
                      className="text-brand-blue-50 hover:text-brand-yellow-500 flex items-center gap-2.5 transition-all duration-200 hover:translate-x-1"
                    >
                      <Clock className="h-4 w-4 text-brand-yellow-500 shrink-0" />
                      <span>Mercado Envíos Flex</span>
                    </Link>
                  </li>
                  <li>
                    <Link
                      href="/servicios/empresas-cuenta-corriente"
                      className="text-brand-blue-50 hover:text-brand-yellow-500 flex items-center gap-2.5 transition-all duration-200 hover:translate-x-1"
                    >
                      <Building2 className="h-4 w-4 text-brand-yellow-500 shrink-0" />
                      <span>Cuenta Corriente Flexible</span>
                    </Link>
                  </li>
                  <li>
                    <Link
                      href="/servicios#ecommerce-24hs"
                      className="text-brand-blue-50 hover:text-brand-yellow-500 flex items-center gap-2.5 transition-all duration-200 hover:translate-x-1"
                    >
                      <Package className="h-4 w-4 text-brand-yellow-500 shrink-0" />
                      <span>E-commerce 24HS</span>
                    </Link>
                  </li>
                  <li>
                    <Link
                      href="/servicios/deposito-fulfillment"
                      className="text-brand-blue-50 hover:text-brand-yellow-500 flex items-center gap-2.5 transition-all duration-200 hover:translate-x-1"
                    >
                      <Store className="h-4 w-4 text-brand-yellow-500 shrink-0" />
                      <span>E-commerce Same Day</span>
                    </Link>
                  </li>
                  <li>
                    <Link
                      href="/servicios"
                      className="text-brand-yellow-500 hover:text-brand-yellow-400 flex items-center gap-2.5 transition-all duration-200 hover:translate-x-1 font-bold"
                    >
                      <Layers className="h-4 w-4 shrink-0" />
                      <span>Ver todos los servicios</span>
                    </Link>
                  </li>
                </ul>
              </div>
            </div>
          </motion.div>

          {/* COLUMN 3: Contact & Hub Operations Info (4 Cols) */}
          <motion.div
            variants={prefersReducedMotion ? {} : FOOTER_COL}
            className="lg:col-span-4 space-y-5"
          >
            <h4 className="font-subheading text-lg tracking-wider text-brand-yellow-500 uppercase border-b border-white/10 pb-2 font-bold">
              Base de Operaciones MDQ
            </h4>

            <div className="space-y-3.5 text-xs text-brand-blue-50 font-sans">
              <div className="flex gap-3 items-start bg-brand-blue/80 p-3 rounded-xl border border-white/15">
                <div className="p-2 bg-white/10 rounded-lg shrink-0 text-brand-yellow-500">
                  <MapPin className="h-4 w-4" />
                </div>
                <div>
                  <p className="font-bold text-white uppercase font-subheading tracking-wider">Centro de Distribución</p>
                  <p className="font-sans text-[13px] text-brand-blue-50 mt-0.5">Friuli 1972, Mar del Plata</p>
                </div>
              </div>

              <div className="flex gap-3 items-start bg-brand-blue/80 p-3 rounded-xl border border-white/15">
                <div className="p-2 bg-white/10 rounded-lg shrink-0 text-brand-yellow-500">
                  <Phone className="h-4 w-4" />
                </div>
                <div>
                  <p className="font-bold text-white uppercase font-subheading tracking-wider">Línea Directa y WhatsApp</p>
                  <a href="tel:+542236602699" className="font-mono text-[13px] font-bold text-brand-yellow-500 hover:underline block mt-0.5">
                    +54 223 660-2699
                  </a>
                </div>
              </div>

              <div className="flex gap-3 items-start bg-brand-blue/80 p-3 rounded-xl border border-white/15">
                <div className="p-2 bg-white/10 rounded-lg shrink-0 text-brand-yellow-500">
                  <Mail className="h-4 w-4" />
                </div>
                <div>
                  <p className="font-bold text-white uppercase font-subheading tracking-wider">Atención Comercial</p>
                  <a href="mailto:matiascejas@enviosdosruedas.com" className="font-sans text-[12px] text-brand-blue-50 hover:text-brand-yellow-500 transition-colors block mt-0.5 break-all">
                    matiascejas@enviosdosruedas.com
                  </a>
                </div>
              </div>

              <div className="flex gap-3 items-start bg-brand-blue/80 p-3 rounded-xl border border-white/15">
                <div className="p-2 bg-white/10 rounded-lg shrink-0 text-brand-yellow-500">
                  <Clock className="h-4 w-4" />
                </div>
                <div className="space-y-1">
                  <p className="font-bold text-white uppercase font-subheading tracking-wider">Horarios de Despacho (Base Central)</p>
                  <div className="text-[12px] font-sans text-brand-blue-50 space-y-0.5">
                    <div className="flex justify-between items-center gap-4">
                      <span>Lunes a Viernes:</span>
                      <span className="font-mono font-bold text-brand-yellow-500">09:00 - 18:00 hs</span>
                    </div>
                    <div className="flex justify-between items-center gap-4">
                      <span>Sábados:</span>
                      <span className="font-mono font-bold text-brand-yellow-500">10:00 - 15:00 hs</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </motion.div>

        </motion.div>

        {/* Separator */}
        <div className="border-t border-white/10 my-10 relative">
          {/* Scroll to Top — continuous float loop */}
          <motion.button
            onClick={scrollToTop}
            className="absolute -top-5 right-4 sm:right-6 bg-brand-yellow-500 hover:bg-brand-yellow-400 text-brand-blue-900 p-2.5 rounded-full shadow-accent-md hover:shadow-cta-glow transition-colors flex items-center justify-center border-2 border-brand-yellow-500 cursor-pointer"
            title="Volver al inicio"
            aria-label="Volver arriba"
            /* Idle float loop */
            animate={prefersReducedMotion ? {} : { y: [0, -5, 0] }}
            transition={
              prefersReducedMotion
                ? {}
                : { duration: 2, ease: 'easeInOut', repeat: Infinity, repeatType: 'loop' }
            }
            /* Tap feedback */
            whileTap={{ scale: 0.92 }}
            whileHover={prefersReducedMotion ? {} : { scale: 1.1, y: -7 }}
          >
            <ArrowUp className="h-4 w-4 font-bold" />
          </motion.button>
        </div>

        {/* BOTTOM SECTION: Legal & Copyright */}
        <div className="flex flex-col md:flex-row justify-between items-center gap-6 text-xs text-brand-blue-50 font-sans">
          <div className="flex flex-wrap justify-center md:justify-start items-center gap-4 sm:gap-6">
            <p className="font-medium text-white">© 2026 Envíos DosRuedas · Mar del Plata, Argentina.</p>
            <Link href="/servicios" className="hover:text-brand-yellow-500 transition-colors text-brand-blue-50">
              Servicios
            </Link>
            <Link href="/cobertura" className="hover:text-brand-yellow-500 transition-colors text-brand-blue-50">
              Cobertura
            </Link>
            <Link href="/guias/envios-flex-mar-del-plata" className="hover:text-brand-yellow-500 transition-colors text-brand-blue-50">
              Guía MercadoLibre Flex
            </Link>
            <Link href="/nosotros/sobre-nosotros" className="hover:text-brand-yellow-500 transition-colors text-brand-blue-50">
              Sobre Nosotros
            </Link>
            <Link href="/nosotros/preguntas-frecuentes" className="hover:text-brand-yellow-500 transition-colors text-brand-blue-50">
              Preguntas Frecuentes
            </Link>
            <Link href="/nosotros/nuestras-redes" className="hover:text-brand-yellow-500 transition-colors text-brand-blue-50">
              Nuestras Redes
            </Link>
          </div>
          <div className="flex flex-wrap justify-center gap-6 shrink-0 text-brand-blue-50">
            <Link href="/terminos-y-condiciones" className="hover:text-brand-yellow-500 transition-colors">
              Términos y Condiciones
            </Link>
            <Link href="/politica-de-privacidad" className="hover:text-brand-yellow-500 transition-colors">
              Política de Privacidad
            </Link>
          </div>
        </div>

      </div>
    </footer>
  );
}

```

### Pricing Constants & Tiers (src/lib/pricing.ts) (`src/lib/pricing.ts`)

```typescript
/**
 * Funciones puras de cálculo de precios para los servicios de Envíos DosRuedas.
 * Al ser puras (sin dependencias de React ni I/O), son completamente testeables.
 */

export interface PriceRangeProp {
  id: number;
  serviceType: string;
  distanciaMinKm: number;
  distanciaMaxKm: number;
  precioRango: number;
  descripcion: string;
}

/** Tramo de tarifa fija: se aplica a distancias mayores que `minKm` y hasta `maxKm` inclusive. */
export interface PriceTier {
  minKm: number;
  maxKm: number;
  price: number;
}

/**
 * Tarifas oficiales 2026 (docs/contexto/precios.md). Son el fallback cuando `PriceRange`
 * está vacía y la única fuente para mostrar tarifas en la UI: no copiar estos valores a mano.
 */
export const EXPRESS_TIERS: readonly PriceTier[] = [
  { minKm: 0, maxKm: 3, price: 3700 },
  { minKm: 3, maxKm: 5, price: 4600 },
  { minKm: 5, maxKm: 7, price: 6100 },
  { minKm: 7, maxKm: 10, price: 8200 },
];
export const EXPRESS_PRICE_PER_KM = 1000;

export const LOW_COST_TIERS: readonly PriceTier[] = [
  { minKm: 0, maxKm: 3, price: 3000 },
  { minKm: 3, maxKm: 5, price: 4000 },
  { minKm: 5, maxKm: 7, price: 5300 },
  { minKm: 7, maxKm: 10, price: 7000 },
];
export const LOW_COST_PRICE_PER_KM = 700;

/**
 * Calcula precio: tramo fijo si distanceKm <= maxKm, sino distanceKm × pricePerKm (lineal).
 * NO usa Math.ceil — corrección dueño octubre 2026: precio por km lineal.
 * Redondea al entero más cercano para evitar problemas de punto flotante.
 */
function fallbackPrice(distanceKm: number, tiers: readonly PriceTier[], pricePerKm: number): number {
  const tier = tiers.find((t) => distanceKm <= t.maxKm);
  return tier ? tier.price : Math.round(distanceKm * pricePerKm);
}

/**
 * Calcula el precio del servicio Express para una distancia dada.
 *
 * Lógica de rangos (según BD):
 *   0–3 km  → $3.700
 *   3–5 km  → $4.600
 *   5–7 km  → $6.100
 *   7–10 km → $8.200
 *   +10 km  → distanceKm × $1.000  (km total × precio por km, LINEAL)
 *
 * @param distanceKm  Distancia en kilómetros (puede tener decimales).
 * @param priceRanges Rangos de precios obtenidos desde la base de datos.
 * @returns El precio en ARS o `'consultar'` si supera los 20 km.
 */
export function calculateExpressPrice(
  distanceKm: number,
  priceRanges: PriceRangeProp[]
): number | 'consultar' {
  if (distanceKm > 20) return 'consultar';

  const expressRanges = priceRanges.filter((r) => r.serviceType === 'EXPRESS');

  if (expressRanges.length > 0) {
    const matchingRange = expressRanges.find(
      (r) => (r.distanciaMinKm === 0 ? distanceKm >= r.distanciaMinKm : distanceKm > r.distanciaMinKm) && distanceKm <= r.distanciaMaxKm
    );

    if (matchingRange) {
      if (matchingRange.distanciaMaxKm === 9999) {
        // Rango extendido (+10 km): cantidad total de km × precio unitario por km (LINEAL)
        return Math.round(distanceKm * matchingRange.precioRango);
      }
      return matchingRange.precioRango;
    }
  } else {
    // Fallback cuando la tabla de precios de la BD está vacía — misma lógica de rangos
    return fallbackPrice(distanceKm, EXPRESS_TIERS, EXPRESS_PRICE_PER_KM);
  }

  return 'consultar';
}

/**
 * Calcula el precio del servicio LowCost para una distancia dada.
 *
 * Lógica de rangos (según BD):
 *   0–3 km  → $3.000
 *   3–5 km  → $4.000
 *   5–7 km  → $5.300
 *   7–10 km → $7.000
 *   +10 km  → distanceKm × $700  (km total × precio por km, LINEAL)
 *
 * @param distanceKm  Distancia en kilómetros (puede tener decimales).
 * @param priceRanges Rangos de precios obtenidos desde la base de datos.
 * @returns El precio en ARS o `'consultar'` si supera los 20 km.
 */
export function calculateLowCostPrice(
  distanceKm: number,
  priceRanges: PriceRangeProp[]
): number | 'consultar' {
  if (distanceKm > 20) return 'consultar';

  const lowCostRanges = priceRanges.filter((r) => r.serviceType === 'LOW_COST');

  if (lowCostRanges.length > 0) {
    const matchingRange = lowCostRanges.find(
      (r) => (r.distanciaMinKm === 0 ? distanceKm >= r.distanciaMinKm : distanceKm > r.distanciaMinKm) && distanceKm <= r.distanciaMaxKm
    );

    if (matchingRange) {
      if (matchingRange.distanciaMaxKm === 9999) {
        // Rango extendido (+10 km): cantidad total de km × precio unitario por km (LINEAL)
        return Math.round(distanceKm * matchingRange.precioRango);
      }
      return matchingRange.precioRango;
    }
  } else {
    // Fallback cuando la tabla de precios de la BD está vacía — misma lógica de rangos
    return fallbackPrice(distanceKm, LOW_COST_TIERS, LOW_COST_PRICE_PER_KM);
  }

  return 'consultar';
}

```

### Business Promises & Service Constants (src/lib/promises.ts) (`src/lib/promises.ts`)

```typescript
/**
 * Constantes únicas de promesas de servicio y umbrales operativos (BL-03).
 * Fuente de verdad unificada para cotizadores, páginas informativas, JSON-LD y llms.txt.
 *
 * Nota: Si se modifican estas promesas, recordar actualizar sincronizadamente también
 * public/llms.txt y public/llms-full.txt.
 *
 * Contexto del dueño (definiciones verbatim de servicio, recargos, protocolos y lo que
 * niega explícitamente): docs/knowledge_base/00-negocio/servicios.md y voz-y-lineas-rojas.md
 */

// Ventana de entrega Express.
// Cambio 2026-09-29 (decisión del dueño, relevamiento con Matías Cejas): la promesa de
// "60 a 90 min" se retiró por inexacta. Express coordina hoy una franja horaria acotada
// a elección del cliente, con 2 hs de anticipación mínima.
//
// Contrato de las dos formas, porque se interpolan en oraciones distintas:
//   EXPRESS_WINDOW       → forma larga. SIEMPRE después de "en" o "Entrega en":
//                          "Entrega en franja horaria de 3 hs".
//   EXPRESS_WINDOW_SHORT → forma compacta, para chips, tablas y rótulos sueltos:
//                          "Franja de 3 hs". NUNCA dentro de una oración con "en",
//                          porque "en 3 hs" se leería como duración de la entrega.
export const EXPRESS_WINDOW = 'franja horaria de 3 hs';
export const EXPRESS_WINDOW_SHORT = 'Franja de 3 hs';

// Anticipación mínima para coordinar una franja de Express.
export const EXPRESS_LEAD_TIME = '2 hs de anticipación';

// Corte Express: pedido hasta esta hora para entregar en el día. El último rango
// posible es 17 a 19 hs (entrevista 2026-09-28 §1.1).
export const EXPRESS_CUTOFF_TIME = '15:00 hs';

// Ventanas operativas LowCost
export const LOWCOST_CUTOFF_TIME = '13:00 hs';
export const LOWCOST_DELIVERY_DEADLINE = '19:00 hs';

// Mercado Envíos Flex
export const FLEX_CUTOFF_TIME = '15:00 hs';
export const FLEX_DELIVERY_DEADLINE = '20:00 hs';

// Tarifas fijas de los niveles Flex. Fuera de `PriceRange`: son precio cerrado
// por nivel, no un rango por distancia. El Nivel 1 no tiene cifra propia —cobra
// la tabla LowCost por zona (ver `LOW_COST_TIERS` en `pricing.ts`).
export const FLEX_NIVEL_2_PRICE = 6500; // Tope fijo en Z4 y Z5
export const FLEX_NIVEL_3_PRICE = 4500; // Tarifa plana a todo Mar del Plata

// Recargo por lluvia. El dueño (entrevista 2026-09-28) define un rango según el
// servicio: 50 % para Express y LowCost, 30 % en todos los demás. Esta constante
// modela SOLO el caso de 30 %, que es el único que hoy se muestra en el sitio.
// Antes de usar este valor para Express o LowCost, agregar el desglose por servicio.
// Ver docs/knowledge_base/00-negocio/tarifas.md §7.
export const RAIN_SURCHARGE_PERCENT = 30;

// Recargo por lluvia para Express y LowCost (el caso de 50 % del rango del dueño).
export const RAIN_SURCHARGE_PERCENT_EXPRESS_LOWCOST = 50;

// Recargos operativos de Express y LowCost (entrevista 2026-09-28 §3). Se informan
// en el cotizador pero no entran en el cálculo automático: dependen de lo que pase
// en el viaje (lluvia, espera, paradas, destinatario ausente).
export const WAIT_TOLERANCE_MIN = 10; // Espera en puerta sin cargo
export const WAIT_CHARGE_ARS = 2200; // Por cada bloque de espera, desde el minuto 11 (corrección dueño oct 2026)
export const WAIT_CHARGE_BLOCK_MIN = 10;
export const EXTRA_STOP_SURCHARGE_PERCENT = 50; // Por parada intermedia sobre la ruta
export const EXTRA_STOP_MAX_DETOUR_KM = 2; // Más desvío que esto es un envío aparte
export const RETRY_CHARGE_PERCENT = 100; // Segunda visita por destinatario ausente

// Periferia: destinos fuera de la urbana de Mar del Plata (Batán, Sierra de los
// Padres…). NO es el excedente de 10 a 20 km de `pricing.ts` ($1.000 / $700 por km):
// es otra tarifa, por km de ruta, que se cotiza aparte. Ver entrevista §3.1.
export const PERIPHERY_PRICE_PER_KM = 1000;
// Bulto extra: más de 5 kg o 40 × 40 × 30 cm. Corrección dueño octubre 2026: desde $1800.
export const BULK_EXTRA_FROM_ARS = 1800;

// Umbrales de distancia y límites físicos
export const CONSULT_THRESHOLD_KM = 20; // Hasta 20 km cálculo automático; > 20 km "A consultar"

// Capacidad por bulto. UN umbral, dos formas de expresarlo:
//   STANDARD_WEIGHT_KG            → lo que entra sin recargo. Es el único número de
//                                   peso que va al copy y a las tarjetas de servicio.
//   STANDARD_BULLET_DIMENSIONS_CM → el mismo umbral en volumen.
//
// Sobrepasado el umbral, el bulto se coordina aparte y entra un recargo desde
// `BULK_EXTRA_FROM_ARS`, cuyo monto final depende del servicio. No entra en el
// cálculo automático del cotizador.
//
// SIN TECHO NUMÉRICO PUBLICADO, y es deliberado (decisión del dueño 2026-09-30).
// Existió una constante `MAX_WEIGHT_KG = 15` que ningún fuente del dueño respalda:
// el 15 kg venía solo del `.docx`, siempre como pregunta sin respuesta registrada
// o como aserción del propio `.docx` — la misma clase de número viejo que el
// dueño ya corrigió ahí ("60-90 min: ESTO ES FALSO"). Lo que el dueño sí
// respondió, textual, fue "todo lo que pueda ser llevado en moto" (CSV pregunta
// 4), sin cifra. Publicar un techo inventado además rompía el recargo por bulto
// extra: si el máximo fuera 5 kg, "más de 5 kg suma $1.800" sería imposible.
// Constante eliminada; el guard de `src/lib/copy-guard.test.ts` la bloquea.
export const STANDARD_WEIGHT_KG = 5;
export const STANDARD_BULLET_DIMENSIONS_CM = '40 × 40 × 30 cm';

// Condiciones comerciales Depósito & Fulfillment (servicio para empresas)
// No figuran en la tabla `PriceRange` ni en docs/contexto/precios.md: son tarifas
// cerradas definidas por el dueño. El 20 % de DropOFF quedó confirmado en el relevamiento
// del 2026-09-29; SAME_DAY_FIXED_PRICE se suma ese mismo día.
export const DROPOFF_DISCOUNT_PERCENT = 20; // Descuento por traer envíos listos al depósito
export const CONTRAREEMBOLSO_COMMISSION_PERCENT = 0; // Sin extra ni comisión por cobro en entrega

// Tarifa fija del plan E-Commerce Same Day para toda la ciudad. Fuera de `PriceRange`
// a propósito: es un precio cerrado por servicio, no un rango por distancia.
export const SAME_DAY_FIXED_PRICE = 6000;

// Tarifa fija E-Commerce 24HS (Next Day) — Confirmada por Matías 2026-09-29.
// Recolección gratis desde 10 envíos. DropOFF -20% solo en este servicio.
export const ECOMMERCE_24HS_PRICE = 3800;

/** Envíos/mes desde los cuales el retiro es gratis. */
export const ECOMMERCE_24HS_FREE_PICKUP_THRESHOLD = 10;

/**
 * Escala de planes E-Commerce 24HS. Vivían como literales dentro de
 * `Ecommerce24HSPricing.tsx`; se movieron acá para que haya una sola fuente,
 * como manda AGENTS.md.
 *
 * Procedencia: `Inicial` es `ECOMMERCE_24HS_PRICE`, confirmado de palabra por el
 * dueño el 2026-09-29. `Pro`, `Elite` y `Partner` salen de la escala que el
 * sitio ya publica; no hay confirmación verbal registrada para esos tres.
 * Si el dueño ajusta la escala, se corrige acá y en ningún otro lado.
 */
export const ECOMMERCE_24HS_PLANS = [
  { name: 'Inicial', fromEnvos: 1, toEnvios: 199, price: ECOMMERCE_24HS_PRICE, featured: false },
  { name: 'Pro', fromEnvos: 200, toEnvios: 1199, price: 3500, featured: true },
  { name: 'Elite', fromEnvos: 1200, toEnvios: 1999, price: 3200, featured: false },
  { name: 'Partner', fromEnvos: 2000, toEnvios: null, price: 3000, featured: false },
] as const;

/**
 * Planes de la landing de Emprendedores. Tarifas cerradas por plan, fuera de
 * `PriceRange`. El Plan Inicial DropOFF ya viene con el -20% aplicado sobre la
 * tarifa plana; el Plan PyME Corporativo no tiene cifra: se cotiza.
 */
export const EMPRENDEDORES_PLANS = [
  {
    name: 'Plan Inicial DropOFF',
    distance: 'Por envío en MDQ',
    price: 2400, // Tarifa base del Plan DropOFF. La consume también `DropoffCalculator`.
    period: '/ envío',
    tag: `DropOFF -${DROPOFF_DISCOUNT_PERCENT}%`,
    note: 'Traés tus paquetes listos a Friuli 1972 y el descuento se aplica solo.',
    featured: false,
  },
  {
    name: 'Plan E-Commerce 3PL',
    distance: 'Stock gratis',
    price: 3000,
    period: '/ envío + stock gratis',
    tag: 'Con depósito',
    note: 'Stock gratis en Friuli 1972 + picking QR + Same Day.',
    featured: true,
  },
  {
    name: 'Plan PyME Corporativo',
    distance: 'Volumen > 10 envíos/día',
    price: null,
    period: '',
    tag: 'Cuenta corriente',
    note: 'Para empresas con envíos diarios recurrentes. La tarifa se cotiza.',
    featured: false,
  },
] as const;

// Reglas de 2da visita / reintento por servicio (corrección dueño octubre 2026)
export const RETRY_RULES = {
  EXPRESS: { type: 'NEW_TRIP', description: 'Se cobra como viaje nuevo' },
  LOW_COST: { type: 'NEW_TRIP', description: 'Se cobra como viaje nuevo' },
  FLEX_NIVEL_1: { type: 'PERCENT', value: 50, description: '50% en todas las zonas' },
  FLEX_NIVEL_2: { type: 'ZONE_BASED', z1: 0, z2_to_z5: 50, description: 'Z1 gratis, Z2-Z5 50%' },
  FLEX_NIVEL_3: { type: 'FREE', description: '100% bonificada todas zonas' },
  DEPOSITO_3PL: { type: 'FREE', description: '100% bonificada' },
  ECOMMERCE_24HS: { type: 'FREE', description: '100% bonificada' },
  CUENTA_CORRIENTE: { type: 'PERCENT', value: 50, description: '50% del valor original' },
} as const;

// Horarios de atención oficiales en base central Friuli 1972 (Decisión 5 aprobada)
export const OPERATING_HOURS = {
  weekdays: '09:00 a 18:00 hs',
  saturdays: '10:00 a 15:00 hs',
  sundays: 'Cerrado',
} as const;

// Canales de contacto oficiales unificados (BL-19)
export const CONTACT_EMAIL = 'matiascejas@enviosdosruedas.com';
export const SUPPORT_PHONE = '+54 223 660-2699';

```

