# Experimental results for [Boost Bloom Library](https://github.com/boostorg/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for several configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-march=native`),
which causes `fast_multiblock32` and `fast_multiblock64` to use their AVX2 variant.

For reference, we provide also insertion, successful lookup and unsuccessful lookup times
for a `boost::unordered_flat_set<int>` with the same number of elements `N`.

## Results

* [GCC 14, x64](#gcc-14-x64)
* [Clang 18, x64](#clang-18-x64)
* [Clang 15, ARM64](#clang-15-arm64)
* [VS 2022, x64](#vs-2022-x64)
* [GCC 14, x86](#gcc-14-x86)
* [Clang 18, x86](#clang-18-x86)
* [VS 2022, x86](#vs-2022-x86)

### GCC 14, x64
<!--gcc-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">38.69</td>
    <td align="right">6.12</td>
    <td align="right">4.36</td>
    <td align="right">13.76</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">11.28</td>
    <td align="right">12.40</td>
    <td align="right">18.37</td>
    <td align="right">17.24</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.17</td>
    <td align="right">4.60</td>
    <td align="right">4.61</td>
    <td align="right">4.60</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">5.14</td>
    <td align="right">5.14</td>
    <td align="right">5.14</td>
    <td align="right">5.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">16.55</td>
    <td align="right">17.91</td>
    <td align="right">19.22</td>
    <td align="right">20.66</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.41</td>
    <td align="right">5.18</td>
    <td align="right">5.18</td>
    <td align="right">5.18</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.44</td>
    <td align="right">5.56</td>
    <td align="right">5.55</td>
    <td align="right">5.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">20.42</td>
    <td align="right">21.73</td>
    <td align="right">18.16</td>
    <td align="right">23.20</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.02</td>
    <td align="right">5.63</td>
    <td align="right">5.63</td>
    <td align="right">5.63</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.55</td>
    <td align="right">6.02</td>
    <td align="right">6.02</td>
    <td align="right">6.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">24.19</td>
    <td align="right">27.71</td>
    <td align="right">18.56</td>
    <td align="right">27.22</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.38</td>
    <td align="right">5.97</td>
    <td align="right">5.97</td>
    <td align="right">5.97</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">5.82</td>
    <td align="right">6.30</td>
    <td align="right">6.30</td>
    <td align="right">6.30</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.00</td>
    <td align="right">5.64</td>
    <td align="right">5.64</td>
    <td align="right">5.64</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">5.53</td>
    <td align="right">6.99</td>
    <td align="right">6.98</td>
    <td align="right">7.01</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">3.24</td>
    <td align="right">2.94</td>
    <td align="right">2.94</td>
    <td align="right">2.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">5.86</td>
    <td align="right">9.25</td>
    <td align="right">9.25</td>
    <td align="right">9.26</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">7.04</td>
    <td align="right">9.68</td>
    <td align="right">9.67</td>
    <td align="right">9.68</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.70</td>
    <td align="right">2.75</td>
    <td align="right">2.75</td>
    <td align="right">2.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">9.14</td>
    <td align="right">11.66</td>
    <td align="right">11.67</td>
    <td align="right">11.76</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">19.11</td>
    <td align="right">13.69</td>
    <td align="right">13.54</td>
    <td align="right">13.70</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">5.80</td>
    <td align="right">5.86</td>
    <td align="right">4.16</td>
    <td align="right">14.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">10.43</td>
    <td align="right">12.73</td>
    <td align="right">12.72</td>
    <td align="right">12.74</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.69</td>
    <td align="right">15.16</td>
    <td align="right">15.17</td>
    <td align="right">15.51</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">5.85</td>
    <td align="right">5.91</td>
    <td align="right">4.15</td>
    <td align="right">14.74</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">3.21</td>
    <td align="right">2.79</td>
    <td align="right">2.79</td>
    <td align="right">2.80</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.65</td>
    <td align="right">4.80</td>
    <td align="right">4.81</td>
    <td align="right">4.80</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.81</td>
    <td align="right">4.60</td>
    <td align="right">4.60</td>
    <td align="right">4.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.36</td>
    <td align="right">2.85</td>
    <td align="right">2.86</td>
    <td align="right">2.85</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.49</td>
    <td align="right">4.19</td>
    <td align="right">4.20</td>
    <td align="right">4.19</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.82</td>
    <td align="right">4.73</td>
    <td align="right">4.72</td>
    <td align="right">4.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">5.57</td>
    <td align="right">5.68</td>
    <td align="right">3.90</td>
    <td align="right">14.34</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.65</td>
    <td align="right">8.26</td>
    <td align="right">6.11</td>
    <td align="right">17.93</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.86</td>
    <td align="right">8.02</td>
    <td align="right">6.07</td>
    <td align="right">17.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.63</td>
    <td align="right">5.71</td>
    <td align="right">3.93</td>
    <td align="right">14.43</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.48</td>
    <td align="right">9.38</td>
    <td align="right">6.16</td>
    <td align="right">18.64</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.64</td>
    <td align="right">9.19</td>
    <td align="right">6.11</td>
    <td align="right">18.29</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.43</td>
    <td align="right">7.34</td>
    <td align="right">14.47</td>
    <td align="right">12.71</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.71</td>
    <td align="right">8.79</td>
    <td align="right">18.84</td>
    <td align="right">15.76</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.23</td>
    <td align="right">10.86</td>
    <td align="right">11.22</td>
    <td align="right">11.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">8.78</td>
    <td align="right">10.40</td>
    <td align="right">14.40</td>
    <td align="right">15.80</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">12.53</td>
    <td align="right">10.50</td>
    <td align="right">16.13</td>
    <td align="right">17.09</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.03</td>
    <td align="right">14.35</td>
    <td align="right">13.76</td>
    <td align="right">14.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">10.66</td>
    <td align="right">11.92</td>
    <td align="right">14.05</td>
    <td align="right">16.78</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.95</td>
    <td align="right">12.95</td>
    <td align="right">17.31</td>
    <td align="right">19.65</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">14.72</td>
    <td align="right">15.69</td>
    <td align="right">15.67</td>
    <td align="right">16.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">12.86</td>
    <td align="right">14.37</td>
    <td align="right">14.76</td>
    <td align="right">18.49</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.62</td>
    <td align="right">15.15</td>
    <td align="right">16.93</td>
    <td align="right">20.05</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">20.67</td>
    <td align="right">20.98</td>
    <td align="right">21.10</td>
    <td align="right">21.27</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">58.45</td>
    <td align="right">23.42</td>
    <td align="right">14.32</td>
    <td align="right">31.35</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">15.72</td>
    <td align="right">17.56</td>
    <td align="right">21.22</td>
    <td align="right">20.81</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">6.46</td>
    <td align="right">7.13</td>
    <td align="right">7.11</td>
    <td align="right">7.11</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.60</td>
    <td align="right">6.32</td>
    <td align="right">6.36</td>
    <td align="right">6.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">53.47</td>
    <td align="right">58.47</td>
    <td align="right">29.20</td>
    <td align="right">45.26</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">11.32</td>
    <td align="right">12.33</td>
    <td align="right">12.33</td>
    <td align="right">12.32</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">12.00</td>
    <td align="right">12.53</td>
    <td align="right">12.54</td>
    <td align="right">12.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">86.50</td>
    <td align="right">94.83</td>
    <td align="right">34.23</td>
    <td align="right">67.11</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">16.57</td>
    <td align="right">18.11</td>
    <td align="right">18.12</td>
    <td align="right">18.10</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">20.21</td>
    <td align="right">20.33</td>
    <td align="right">20.33</td>
    <td align="right">20.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">129.60</td>
    <td align="right">142.01</td>
    <td align="right">41.07</td>
    <td align="right">96.15</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">22.38</td>
    <td align="right">21.84</td>
    <td align="right">21.97</td>
    <td align="right">23.90</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">22.98</td>
    <td align="right">25.28</td>
    <td align="right">25.29</td>
    <td align="right">25.31</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.93</td>
    <td align="right">7.58</td>
    <td align="right">7.60</td>
    <td align="right">7.58</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">8.95</td>
    <td align="right">10.70</td>
    <td align="right">10.71</td>
    <td align="right">10.72</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">4.19</td>
    <td align="right">3.96</td>
    <td align="right">4.00</td>
    <td align="right">4.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">13.27</td>
    <td align="right">16.66</td>
    <td align="right">16.63</td>
    <td align="right">16.65</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">15.95</td>
    <td align="right">20.06</td>
    <td align="right">20.00</td>
    <td align="right">20.00</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.90</td>
    <td align="right">8.17</td>
    <td align="right">8.18</td>
    <td align="right">8.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">29.49</td>
    <td align="right">30.51</td>
    <td align="right">30.52</td>
    <td align="right">30.54</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">35.15</td>
    <td align="right">34.48</td>
    <td align="right">34.51</td>
    <td align="right">34.52</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">19.11</td>
    <td align="right">20.54</td>
    <td align="right">14.90</td>
    <td align="right">25.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">38.92</td>
    <td align="right">39.54</td>
    <td align="right">39.53</td>
    <td align="right">39.57</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.97</td>
    <td align="right">51.73</td>
    <td align="right">51.21</td>
    <td align="right">50.56</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">22.27</td>
    <td align="right">23.81</td>
    <td align="right">16.81</td>
    <td align="right">28.51</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">4.28</td>
    <td align="right">3.95</td>
    <td align="right">3.94</td>
    <td align="right">3.95</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">6.07</td>
    <td align="right">6.40</td>
    <td align="right">6.39</td>
    <td align="right">6.33</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">6.09</td>
    <td align="right">6.15</td>
    <td align="right">6.15</td>
    <td align="right">6.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">9.04</td>
    <td align="right">8.80</td>
    <td align="right">8.83</td>
    <td align="right">8.81</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.35</td>
    <td align="right">10.36</td>
    <td align="right">10.41</td>
    <td align="right">10.34</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.94</td>
    <td align="right">12.08</td>
    <td align="right">12.08</td>
    <td align="right">12.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">18.68</td>
    <td align="right">20.39</td>
    <td align="right">14.63</td>
    <td align="right">24.65</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">24.90</td>
    <td align="right">26.10</td>
    <td align="right">21.45</td>
    <td align="right">30.76</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">24.03</td>
    <td align="right">26.44</td>
    <td align="right">21.83</td>
    <td align="right">30.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">22.04</td>
    <td align="right">23.73</td>
    <td align="right">16.56</td>
    <td align="right">27.92</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">32.35</td>
    <td align="right">36.28</td>
    <td align="right">24.80</td>
    <td align="right">36.63</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">31.76</td>
    <td align="right">36.22</td>
    <td align="right">24.91</td>
    <td align="right">36.37</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">8.23</td>
    <td align="right">9.07</td>
    <td align="right">15.91</td>
    <td align="right">15.06</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">13.21</td>
    <td align="right">10.98</td>
    <td align="right">20.77</td>
    <td align="right">18.41</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">14.07</td>
    <td align="right">14.24</td>
    <td align="right">14.28</td>
    <td align="right">14.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">14.98</td>
    <td align="right">16.69</td>
    <td align="right">17.82</td>
    <td align="right">21.03</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">21.68</td>
    <td align="right">20.21</td>
    <td align="right">21.25</td>
    <td align="right">24.56</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">30.22</td>
    <td align="right">31.80</td>
    <td align="right">31.82</td>
    <td align="right">31.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">27.34</td>
    <td align="right">27.86</td>
    <td align="right">21.72</td>
    <td align="right">30.98</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">34.96</td>
    <td align="right">33.33</td>
    <td align="right">26.39</td>
    <td align="right">36.99</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">45.59</td>
    <td align="right">49.83</td>
    <td align="right">49.79</td>
    <td align="right">49.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">41.75</td>
    <td align="right">42.38</td>
    <td align="right">24.92</td>
    <td align="right">42.41</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">50.90</td>
    <td align="right">50.31</td>
    <td align="right">29.22</td>
    <td align="right">48.36</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">74.94</td>
    <td align="right">74.31</td>
    <td align="right">74.23</td>
    <td align="right">74.30</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.23</td>
    <td align="right">6.03</td>
    <td align="right">4.31</td>
    <td align="right">13.13</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.36</td>
    <td align="right">10.89</td>
    <td align="right">17.98</td>
    <td align="right">15.71</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.07</td>
    <td align="right">4.11</td>
    <td align="right">4.10</td>
    <td align="right">4.10</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.07</td>
    <td align="right">4.61</td>
    <td align="right">4.60</td>
    <td align="right">4.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.83</td>
    <td align="right">16.26</td>
    <td align="right">18.60</td>
    <td align="right">19.88</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.55</td>
    <td align="right">4.70</td>
    <td align="right">4.69</td>
    <td align="right">4.69</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.56</td>
    <td align="right">5.27</td>
    <td align="right">5.27</td>
    <td align="right">5.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.80</td>
    <td align="right">19.94</td>
    <td align="right">17.49</td>
    <td align="right">22.51</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.00</td>
    <td align="right">5.30</td>
    <td align="right">5.30</td>
    <td align="right">5.30</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">4.94</td>
    <td align="right">5.74</td>
    <td align="right">5.74</td>
    <td align="right">5.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">23.31</td>
    <td align="right">24.02</td>
    <td align="right">18.26</td>
    <td align="right">24.54</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.42</td>
    <td align="right">5.75</td>
    <td align="right">5.75</td>
    <td align="right">5.75</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">3.31</td>
    <td align="right">3.47</td>
    <td align="right">3.45</td>
    <td align="right">3.45</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">3.26</td>
    <td align="right">3.88</td>
    <td align="right">3.88</td>
    <td align="right">3.88</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">3.34</td>
    <td align="right">3.70</td>
    <td align="right">3.72</td>
    <td align="right">3.71</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.89</td>
    <td align="right">2.70</td>
    <td align="right">2.68</td>
    <td align="right">2.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">3.39</td>
    <td align="right">4.82</td>
    <td align="right">4.82</td>
    <td align="right">4.81</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">4.08</td>
    <td align="right">4.96</td>
    <td align="right">4.95</td>
    <td align="right">4.95</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.77</td>
    <td align="right">2.49</td>
    <td align="right">2.50</td>
    <td align="right">2.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">5.87</td>
    <td align="right">7.76</td>
    <td align="right">7.69</td>
    <td align="right">7.74</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">6.03</td>
    <td align="right">7.53</td>
    <td align="right">7.50</td>
    <td align="right">7.51</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.41</td>
    <td align="right">4.53</td>
    <td align="right">3.36</td>
    <td align="right">13.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">6.25</td>
    <td align="right">8.25</td>
    <td align="right">8.25</td>
    <td align="right">8.25</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">6.97</td>
    <td align="right">8.39</td>
    <td align="right">8.39</td>
    <td align="right">8.37</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.46</td>
    <td align="right">4.55</td>
    <td align="right">3.34</td>
    <td align="right">13.94</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.85</td>
    <td align="right">2.49</td>
    <td align="right">2.49</td>
    <td align="right">2.50</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.92</td>
    <td align="right">4.20</td>
    <td align="right">4.20</td>
    <td align="right">4.20</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.06</td>
    <td align="right">4.04</td>
    <td align="right">4.04</td>
    <td align="right">4.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.95</td>
    <td align="right">2.54</td>
    <td align="right">2.54</td>
    <td align="right">2.55</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.50</td>
    <td align="right">3.89</td>
    <td align="right">3.90</td>
    <td align="right">3.90</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.28</td>
    <td align="right">4.15</td>
    <td align="right">4.14</td>
    <td align="right">4.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.48</td>
    <td align="right">4.23</td>
    <td align="right">3.18</td>
    <td align="right">13.46</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">5.84</td>
    <td align="right">6.31</td>
    <td align="right">5.19</td>
    <td align="right">16.57</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">6.07</td>
    <td align="right">6.16</td>
    <td align="right">4.98</td>
    <td align="right">16.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.51</td>
    <td align="right">4.26</td>
    <td align="right">3.15</td>
    <td align="right">13.39</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">6.98</td>
    <td align="right">7.30</td>
    <td align="right">5.33</td>
    <td align="right">17.35</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.27</td>
    <td align="right">7.05</td>
    <td align="right">5.08</td>
    <td align="right">16.92</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.34</td>
    <td align="right">6.69</td>
    <td align="right">14.48</td>
    <td align="right">12.48</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.77</td>
    <td align="right">7.93</td>
    <td align="right">18.16</td>
    <td align="right">15.28</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.28</td>
    <td align="right">10.37</td>
    <td align="right">10.38</td>
    <td align="right">10.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.69</td>
    <td align="right">9.08</td>
    <td align="right">13.50</td>
    <td align="right">14.44</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.58</td>
    <td align="right">9.31</td>
    <td align="right">15.37</td>
    <td align="right">16.17</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.86</td>
    <td align="right">14.31</td>
    <td align="right">14.29</td>
    <td align="right">14.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.99</td>
    <td align="right">10.65</td>
    <td align="right">13.18</td>
    <td align="right">15.74</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">15.53</td>
    <td align="right">12.06</td>
    <td align="right">16.44</td>
    <td align="right">18.48</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.46</td>
    <td align="right">15.69</td>
    <td align="right">15.83</td>
    <td align="right">16.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.33</td>
    <td align="right">13.37</td>
    <td align="right">14.31</td>
    <td align="right">17.46</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">17.21</td>
    <td align="right">13.67</td>
    <td align="right">15.82</td>
    <td align="right">19.67</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.95</td>
    <td align="right">20.64</td>
    <td align="right">20.76</td>
    <td align="right">21.16</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">52.19</td>
    <td align="right">23.72</td>
    <td align="right">14.42</td>
    <td align="right">31.47</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">16.44</td>
    <td align="right">17.00</td>
    <td align="right">21.25</td>
    <td align="right">19.92</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.24</td>
    <td align="right">5.28</td>
    <td align="right">5.24</td>
    <td align="right">5.25</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.62</td>
    <td align="right">6.22</td>
    <td align="right">6.21</td>
    <td align="right">6.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">43.25</td>
    <td align="right">44.37</td>
    <td align="right">25.23</td>
    <td align="right">36.21</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.51</td>
    <td align="right">10.53</td>
    <td align="right">10.58</td>
    <td align="right">10.52</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.16</td>
    <td align="right">12.16</td>
    <td align="right">12.17</td>
    <td align="right">12.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">83.90</td>
    <td align="right">85.53</td>
    <td align="right">31.15</td>
    <td align="right">61.14</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">17.99</td>
    <td align="right">18.01</td>
    <td align="right">18.02</td>
    <td align="right">18.04</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">17.14</td>
    <td align="right">18.96</td>
    <td align="right">18.95</td>
    <td align="right">18.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">120.83</td>
    <td align="right">119.22</td>
    <td align="right">36.83</td>
    <td align="right">81.39</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">22.03</td>
    <td align="right">21.75</td>
    <td align="right">21.74</td>
    <td align="right">21.74</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">14.69</td>
    <td align="right">15.29</td>
    <td align="right">15.25</td>
    <td align="right">15.27</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">4.05</td>
    <td align="right">4.82</td>
    <td align="right">4.81</td>
    <td align="right">4.80</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">4.50</td>
    <td align="right">5.09</td>
    <td align="right">5.11</td>
    <td align="right">5.10</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.53</td>
    <td align="right">3.43</td>
    <td align="right">3.41</td>
    <td align="right">3.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">8.71</td>
    <td align="right">10.40</td>
    <td align="right">10.36</td>
    <td align="right">10.39</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">8.86</td>
    <td align="right">11.20</td>
    <td align="right">11.16</td>
    <td align="right">11.16</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.33</td>
    <td align="right">7.02</td>
    <td align="right">7.03</td>
    <td align="right">7.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">20.10</td>
    <td align="right">23.09</td>
    <td align="right">22.93</td>
    <td align="right">22.82</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">19.12</td>
    <td align="right">22.88</td>
    <td align="right">22.85</td>
    <td align="right">22.85</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">14.89</td>
    <td align="right">15.97</td>
    <td align="right">12.17</td>
    <td align="right">21.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">23.97</td>
    <td align="right">29.55</td>
    <td align="right">29.60</td>
    <td align="right">29.60</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">24.86</td>
    <td align="right">30.64</td>
    <td align="right">30.66</td>
    <td align="right">30.65</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">17.42</td>
    <td align="right">18.30</td>
    <td align="right">13.94</td>
    <td align="right">24.01</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.81</td>
    <td align="right">3.59</td>
    <td align="right">3.63</td>
    <td align="right">3.62</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.84</td>
    <td align="right">5.32</td>
    <td align="right">5.32</td>
    <td align="right">5.32</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">5.75</td>
    <td align="right">6.10</td>
    <td align="right">6.14</td>
    <td align="right">6.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.46</td>
    <td align="right">7.43</td>
    <td align="right">7.44</td>
    <td align="right">7.43</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.10</td>
    <td align="right">9.72</td>
    <td align="right">9.70</td>
    <td align="right">9.68</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.47</td>
    <td align="right">11.75</td>
    <td align="right">11.74</td>
    <td align="right">11.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">14.59</td>
    <td align="right">16.22</td>
    <td align="right">12.03</td>
    <td align="right">20.85</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">20.01</td>
    <td align="right">21.17</td>
    <td align="right">16.94</td>
    <td align="right">27.27</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">18.72</td>
    <td align="right">20.93</td>
    <td align="right">16.77</td>
    <td align="right">26.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">16.59</td>
    <td align="right">18.12</td>
    <td align="right">13.36</td>
    <td align="right">23.11</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">25.07</td>
    <td align="right">29.29</td>
    <td align="right">20.05</td>
    <td align="right">32.62</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">25.52</td>
    <td align="right">26.98</td>
    <td align="right">19.36</td>
    <td align="right">31.83</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">8.13</td>
    <td align="right">8.40</td>
    <td align="right">16.00</td>
    <td align="right">14.82</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.71</td>
    <td align="right">9.42</td>
    <td align="right">19.40</td>
    <td align="right">17.29</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">14.93</td>
    <td align="right">14.97</td>
    <td align="right">15.04</td>
    <td align="right">15.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">16.99</td>
    <td align="right">15.57</td>
    <td align="right">17.48</td>
    <td align="right">20.52</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">23.88</td>
    <td align="right">19.86</td>
    <td align="right">19.73</td>
    <td align="right">24.35</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">28.40</td>
    <td align="right">29.33</td>
    <td align="right">29.38</td>
    <td align="right">29.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">28.25</td>
    <td align="right">26.02</td>
    <td align="right">21.15</td>
    <td align="right">28.65</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">35.97</td>
    <td align="right">32.42</td>
    <td align="right">24.87</td>
    <td align="right">34.74</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">45.20</td>
    <td align="right">47.94</td>
    <td align="right">47.82</td>
    <td align="right">47.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">42.94</td>
    <td align="right">35.55</td>
    <td align="right">24.52</td>
    <td align="right">38.32</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">51.93</td>
    <td align="right">39.76</td>
    <td align="right">26.21</td>
    <td align="right">43.23</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">78.14</td>
    <td align="right">72.15</td>
    <td align="right">72.52</td>
    <td align="right">72.60</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">18.45</td>
    <td align="right">2.52</td>
    <td align="right">1.98</td>
    <td align="right">9.55</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">6.41</td>
    <td align="right">4.15</td>
    <td align="right">11.39</td>
    <td align="right">8.78</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.30</td>
    <td align="right">1.23</td>
    <td align="right">1.23</td>
    <td align="right">1.23</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.62</td>
    <td align="right">1.29</td>
    <td align="right">1.29</td>
    <td align="right">1.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">9.46</td>
    <td align="right">6.10</td>
    <td align="right">11.99</td>
    <td align="right">10.49</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.42</td>
    <td align="right">1.42</td>
    <td align="right">1.42</td>
    <td align="right">1.42</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.70</td>
    <td align="right">1.42</td>
    <td align="right">1.42</td>
    <td align="right">1.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">11.64</td>
    <td align="right">7.35</td>
    <td align="right">11.17</td>
    <td align="right">11.08</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.61</td>
    <td align="right">1.63</td>
    <td align="right">1.63</td>
    <td align="right">1.63</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.74</td>
    <td align="right">1.58</td>
    <td align="right">1.58</td>
    <td align="right">1.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">15.02</td>
    <td align="right">9.34</td>
    <td align="right">11.37</td>
    <td align="right">12.49</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.79</td>
    <td align="right">1.80</td>
    <td align="right">1.80</td>
    <td align="right">1.81</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.80</td>
    <td align="right">1.58</td>
    <td align="right">1.57</td>
    <td align="right">1.58</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.27</td>
    <td align="right">1.69</td>
    <td align="right">1.68</td>
    <td align="right">1.69</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.31</td>
    <td align="right">1.77</td>
    <td align="right">1.76</td>
    <td align="right">1.75</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.02</td>
    <td align="right">1.70</td>
    <td align="right">1.68</td>
    <td align="right">1.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.18</td>
    <td align="right">1.85</td>
    <td align="right">1.86</td>
    <td align="right">1.84</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.70</td>
    <td align="right">2.15</td>
    <td align="right">2.15</td>
    <td align="right">2.24</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.54</td>
    <td align="right">1.40</td>
    <td align="right">1.40</td>
    <td align="right">1.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.06</td>
    <td align="right">2.93</td>
    <td align="right">2.93</td>
    <td align="right">2.91</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.05</td>
    <td align="right">3.02</td>
    <td align="right">3.02</td>
    <td align="right">3.02</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">2.91</td>
    <td align="right">2.41</td>
    <td align="right">1.75</td>
    <td align="right">11.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.51</td>
    <td align="right">3.36</td>
    <td align="right">3.36</td>
    <td align="right">3.36</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.67</td>
    <td align="right">3.58</td>
    <td align="right">3.56</td>
    <td align="right">3.57</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">2.90</td>
    <td align="right">2.92</td>
    <td align="right">1.73</td>
    <td align="right">11.42</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.02</td>
    <td align="right">1.69</td>
    <td align="right">1.68</td>
    <td align="right">1.69</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.26</td>
    <td align="right">1.69</td>
    <td align="right">1.69</td>
    <td align="right">1.70</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.26</td>
    <td align="right">1.74</td>
    <td align="right">1.75</td>
    <td align="right">1.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.03</td>
    <td align="right">1.58</td>
    <td align="right">1.59</td>
    <td align="right">1.59</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.19</td>
    <td align="right">1.86</td>
    <td align="right">1.86</td>
    <td align="right">1.86</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.81</td>
    <td align="right">2.15</td>
    <td align="right">2.15</td>
    <td align="right">2.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">2.95</td>
    <td align="right">2.38</td>
    <td align="right">1.74</td>
    <td align="right">11.30</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.11</td>
    <td align="right">2.91</td>
    <td align="right">2.91</td>
    <td align="right">2.91</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.11</td>
    <td align="right">3.04</td>
    <td align="right">3.04</td>
    <td align="right">3.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.90</td>
    <td align="right">2.87</td>
    <td align="right">1.73</td>
    <td align="right">11.39</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.54</td>
    <td align="right">3.35</td>
    <td align="right">3.38</td>
    <td align="right">3.37</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.77</td>
    <td align="right">3.57</td>
    <td align="right">3.58</td>
    <td align="right">3.57</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">3.21</td>
    <td align="right">3.26</td>
    <td align="right">10.16</td>
    <td align="right">8.46</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">6.96</td>
    <td align="right">3.91</td>
    <td align="right">12.75</td>
    <td align="right">9.39</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">7.72</td>
    <td align="right">4.88</td>
    <td align="right">4.88</td>
    <td align="right">4.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">4.37</td>
    <td align="right">4.36</td>
    <td align="right">9.94</td>
    <td align="right">9.45</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">7.38</td>
    <td align="right">4.52</td>
    <td align="right">10.57</td>
    <td align="right">10.21</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">10.88</td>
    <td align="right">6.79</td>
    <td align="right">6.79</td>
    <td align="right">6.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">5.51</td>
    <td align="right">5.26</td>
    <td align="right">9.77</td>
    <td align="right">9.91</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">8.54</td>
    <td align="right">5.75</td>
    <td align="right">11.26</td>
    <td align="right">10.87</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">12.05</td>
    <td align="right">7.55</td>
    <td align="right">7.55</td>
    <td align="right">7.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">6.99</td>
    <td align="right">6.29</td>
    <td align="right">10.22</td>
    <td align="right">10.57</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">9.42</td>
    <td align="right">6.37</td>
    <td align="right">10.75</td>
    <td align="right">11.35</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">17.20</td>
    <td align="right">10.71</td>
    <td align="right">10.73</td>
    <td align="right">10.68</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">23.99</td>
    <td align="right">11.51</td>
    <td align="right">6.22</td>
    <td align="right">15.79</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">7.74</td>
    <td align="right">6.32</td>
    <td align="right">13.12</td>
    <td align="right">10.51</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">2.09</td>
    <td align="right">2.04</td>
    <td align="right">2.04</td>
    <td align="right">2.05</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">2.16</td>
    <td align="right">2.07</td>
    <td align="right">2.07</td>
    <td align="right">2.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">13.57</td>
    <td align="right">11.66</td>
    <td align="right">16.07</td>
    <td align="right">14.82</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">3.85</td>
    <td align="right">3.55</td>
    <td align="right">3.67</td>
    <td align="right">3.93</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">3.31</td>
    <td align="right">3.27</td>
    <td align="right">3.17</td>
    <td align="right">3.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">31.29</td>
    <td align="right">25.48</td>
    <td align="right">18.70</td>
    <td align="right">22.36</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">7.19</td>
    <td align="right">6.64</td>
    <td align="right">6.70</td>
    <td align="right">6.60</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">6.90</td>
    <td align="right">5.93</td>
    <td align="right">6.21</td>
    <td align="right">6.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">53.23</td>
    <td align="right">39.33</td>
    <td align="right">20.82</td>
    <td align="right">31.67</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">8.91</td>
    <td align="right">7.90</td>
    <td align="right">8.01</td>
    <td align="right">8.26</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">7.93</td>
    <td align="right">6.67</td>
    <td align="right">6.44</td>
    <td align="right">6.43</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.73</td>
    <td align="right">2.61</td>
    <td align="right">2.61</td>
    <td align="right">2.59</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.73</td>
    <td align="right">2.65</td>
    <td align="right">2.62</td>
    <td align="right">2.64</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">2.39</td>
    <td align="right">2.55</td>
    <td align="right">2.55</td>
    <td align="right">2.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.75</td>
    <td align="right">4.14</td>
    <td align="right">4.06</td>
    <td align="right">4.12</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.26</td>
    <td align="right">4.66</td>
    <td align="right">4.52</td>
    <td align="right">4.54</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">2.82</td>
    <td align="right">3.71</td>
    <td align="right">3.71</td>
    <td align="right">3.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">10.82</td>
    <td align="right">10.01</td>
    <td align="right">10.18</td>
    <td align="right">9.77</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">11.28</td>
    <td align="right">9.50</td>
    <td align="right">9.32</td>
    <td align="right">9.20</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">8.25</td>
    <td align="right">8.43</td>
    <td align="right">5.53</td>
    <td align="right">15.25</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">15.68</td>
    <td align="right">13.11</td>
    <td align="right">13.04</td>
    <td align="right">13.41</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">16.48</td>
    <td align="right">13.48</td>
    <td align="right">13.56</td>
    <td align="right">14.48</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">10.19</td>
    <td align="right">11.28</td>
    <td align="right">6.48</td>
    <td align="right">16.63</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">2.40</td>
    <td align="right">2.57</td>
    <td align="right">2.58</td>
    <td align="right">2.58</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.74</td>
    <td align="right">2.59</td>
    <td align="right">2.59</td>
    <td align="right">2.60</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.76</td>
    <td align="right">2.67</td>
    <td align="right">2.63</td>
    <td align="right">2.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">2.92</td>
    <td align="right">3.16</td>
    <td align="right">3.15</td>
    <td align="right">3.40</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">4.43</td>
    <td align="right">4.31</td>
    <td align="right">4.08</td>
    <td align="right">4.08</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.17</td>
    <td align="right">4.60</td>
    <td align="right">4.52</td>
    <td align="right">4.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">7.41</td>
    <td align="right">8.09</td>
    <td align="right">5.52</td>
    <td align="right">14.92</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">11.19</td>
    <td align="right">10.18</td>
    <td align="right">9.99</td>
    <td align="right">9.87</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">10.69</td>
    <td align="right">9.99</td>
    <td align="right">9.84</td>
    <td align="right">9.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">10.48</td>
    <td align="right">11.22</td>
    <td align="right">6.59</td>
    <td align="right">16.67</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">15.33</td>
    <td align="right">12.50</td>
    <td align="right">12.13</td>
    <td align="right">12.87</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">16.09</td>
    <td align="right">13.86</td>
    <td align="right">13.71</td>
    <td align="right">14.07</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">4.70</td>
    <td align="right">4.40</td>
    <td align="right">11.42</td>
    <td align="right">9.97</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">8.96</td>
    <td align="right">4.99</td>
    <td align="right">13.60</td>
    <td align="right">10.65</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">9.08</td>
    <td align="right">6.99</td>
    <td align="right">7.02</td>
    <td align="right">6.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">9.00</td>
    <td align="right">9.51</td>
    <td align="right">13.16</td>
    <td align="right">13.94</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">13.50</td>
    <td align="right">7.98</td>
    <td align="right">13.05</td>
    <td align="right">14.08</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">14.77</td>
    <td align="right">12.44</td>
    <td align="right">12.20</td>
    <td align="right">12.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">16.37</td>
    <td align="right">14.16</td>
    <td align="right">14.53</td>
    <td align="right">17.63</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">23.96</td>
    <td align="right">16.36</td>
    <td align="right">16.57</td>
    <td align="right">20.60</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">27.80</td>
    <td align="right">23.29</td>
    <td align="right">20.98</td>
    <td align="right">20.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">20.49</td>
    <td align="right">16.22</td>
    <td align="right">14.99</td>
    <td align="right">20.16</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">27.11</td>
    <td align="right">18.97</td>
    <td align="right">16.32</td>
    <td align="right">23.09</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">45.68</td>
    <td align="right">35.58</td>
    <td align="right">35.53</td>
    <td align="right">35.57</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">25.12</td>
    <td align="right">5.18</td>
    <td align="right">3.65</td>
    <td align="right">10.52</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.29</td>
    <td align="right">11.38</td>
    <td align="right">14.22</td>
    <td align="right">15.46</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.84</td>
    <td align="right">3.60</td>
    <td align="right">3.59</td>
    <td align="right">3.59</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.37</td>
    <td align="right">4.15</td>
    <td align="right">4.14</td>
    <td align="right">4.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.11</td>
    <td align="right">16.22</td>
    <td align="right">15.01</td>
    <td align="right">17.21</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.47</td>
    <td align="right">4.02</td>
    <td align="right">4.01</td>
    <td align="right">3.98</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.02</td>
    <td align="right">4.76</td>
    <td align="right">4.74</td>
    <td align="right">4.70</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.23</td>
    <td align="right">20.39</td>
    <td align="right">13.99</td>
    <td align="right">19.46</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">7.82</td>
    <td align="right">4.37</td>
    <td align="right">4.33</td>
    <td align="right">4.33</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">6.35</td>
    <td align="right">6.08</td>
    <td align="right">6.06</td>
    <td align="right">6.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">26.31</td>
    <td align="right">24.80</td>
    <td align="right">14.36</td>
    <td align="right">22.01</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">9.21</td>
    <td align="right">4.71</td>
    <td align="right">4.71</td>
    <td align="right">4.71</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">11.97</td>
    <td align="right">5.59</td>
    <td align="right">5.57</td>
    <td align="right">5.56</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.39</td>
    <td align="right">4.30</td>
    <td align="right">4.31</td>
    <td align="right">4.30</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">7.49</td>
    <td align="right">4.65</td>
    <td align="right">4.63</td>
    <td align="right">4.64</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.85</td>
    <td align="right">2.19</td>
    <td align="right">2.19</td>
    <td align="right">2.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">8.26</td>
    <td align="right">7.01</td>
    <td align="right">6.98</td>
    <td align="right">6.94</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">12.77</td>
    <td align="right">7.09</td>
    <td align="right">7.08</td>
    <td align="right">11.96</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.82</td>
    <td align="right">2.99</td>
    <td align="right">2.38</td>
    <td align="right">8.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">13.77</td>
    <td align="right">9.31</td>
    <td align="right">9.22</td>
    <td align="right">9.14</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">15.01</td>
    <td align="right">10.29</td>
    <td align="right">10.31</td>
    <td align="right">10.39</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.30</td>
    <td align="right">4.44</td>
    <td align="right">3.11</td>
    <td align="right">11.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">17.87</td>
    <td align="right">10.39</td>
    <td align="right">10.35</td>
    <td align="right">10.30</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">13.87</td>
    <td align="right">12.24</td>
    <td align="right">12.19</td>
    <td align="right">12.21</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.69</td>
    <td align="right">4.49</td>
    <td align="right">3.07</td>
    <td align="right">11.37</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.81</td>
    <td align="right">2.04</td>
    <td align="right">2.04</td>
    <td align="right">2.04</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.71</td>
    <td align="right">3.26</td>
    <td align="right">3.26</td>
    <td align="right">3.26</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.77</td>
    <td align="right">3.12</td>
    <td align="right">3.12</td>
    <td align="right">3.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.24</td>
    <td align="right">3.41</td>
    <td align="right">2.74</td>
    <td align="right">9.45</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">4.18</td>
    <td align="right">3.87</td>
    <td align="right">3.23</td>
    <td align="right">10.39</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">5.69</td>
    <td align="right">4.63</td>
    <td align="right">3.91</td>
    <td align="right">10.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">6.24</td>
    <td align="right">4.35</td>
    <td align="right">2.98</td>
    <td align="right">10.53</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.90</td>
    <td align="right">6.37</td>
    <td align="right">4.97</td>
    <td align="right">13.25</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.72</td>
    <td align="right">6.29</td>
    <td align="right">5.04</td>
    <td align="right">12.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.46</td>
    <td align="right">4.36</td>
    <td align="right">3.00</td>
    <td align="right">10.59</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">7.85</td>
    <td align="right">7.10</td>
    <td align="right">5.15</td>
    <td align="right">13.85</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">17.22</td>
    <td align="right">6.86</td>
    <td align="right">5.09</td>
    <td align="right">13.41</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">7.09</td>
    <td align="right">6.72</td>
    <td align="right">11.26</td>
    <td align="right">10.51</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">9.82</td>
    <td align="right">8.93</td>
    <td align="right">14.08</td>
    <td align="right">12.78</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.07</td>
    <td align="right">8.92</td>
    <td align="right">8.96</td>
    <td align="right">8.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.44</td>
    <td align="right">9.79</td>
    <td align="right">11.91</td>
    <td align="right">12.94</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">11.82</td>
    <td align="right">11.15</td>
    <td align="right">13.47</td>
    <td align="right">14.46</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.66</td>
    <td align="right">12.91</td>
    <td align="right">12.92</td>
    <td align="right">12.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.36</td>
    <td align="right">11.34</td>
    <td align="right">11.76</td>
    <td align="right">14.21</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">18.26</td>
    <td align="right">13.28</td>
    <td align="right">12.81</td>
    <td align="right">15.48</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">19.53</td>
    <td align="right">15.36</td>
    <td align="right">15.38</td>
    <td align="right">15.31</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.65</td>
    <td align="right">13.75</td>
    <td align="right">12.36</td>
    <td align="right">16.58</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.41</td>
    <td align="right">15.15</td>
    <td align="right">12.44</td>
    <td align="right">16.98</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">26.46</td>
    <td align="right">22.86</td>
    <td align="right">23.02</td>
    <td align="right">22.76</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">42.13</td>
    <td align="right">23.25</td>
    <td align="right">13.60</td>
    <td align="right">27.91</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">10.99</td>
    <td align="right">11.87</td>
    <td align="right">15.63</td>
    <td align="right">15.21</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">7.17</td>
    <td align="right">6.39</td>
    <td align="right">6.45</td>
    <td align="right">6.33</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.80</td>
    <td align="right">4.71</td>
    <td align="right">4.66</td>
    <td align="right">4.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">26.25</td>
    <td align="right">41.94</td>
    <td align="right">20.92</td>
    <td align="right">32.67</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">6.77</td>
    <td align="right">7.56</td>
    <td align="right">7.43</td>
    <td align="right">7.35</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">7.12</td>
    <td align="right">6.76</td>
    <td align="right">6.63</td>
    <td align="right">6.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">68.42</td>
    <td align="right">79.42</td>
    <td align="right">25.90</td>
    <td align="right">54.78</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">15.42</td>
    <td align="right">13.50</td>
    <td align="right">13.51</td>
    <td align="right">13.55</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.30</td>
    <td align="right">15.69</td>
    <td align="right">15.87</td>
    <td align="right">15.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">103.37</td>
    <td align="right">117.71</td>
    <td align="right">31.10</td>
    <td align="right">77.12</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">20.12</td>
    <td align="right">18.81</td>
    <td align="right">18.84</td>
    <td align="right">18.75</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">20.75</td>
    <td align="right">22.58</td>
    <td align="right">22.60</td>
    <td align="right">22.58</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.10</td>
    <td align="right">4.71</td>
    <td align="right">4.71</td>
    <td align="right">4.64</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.72</td>
    <td align="right">5.11</td>
    <td align="right">5.03</td>
    <td align="right">4.97</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.18</td>
    <td align="right">6.06</td>
    <td align="right">6.11</td>
    <td align="right">6.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">11.07</td>
    <td align="right">9.45</td>
    <td align="right">9.19</td>
    <td align="right">9.22</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">16.66</td>
    <td align="right">11.78</td>
    <td align="right">11.55</td>
    <td align="right">11.54</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">5.64</td>
    <td align="right">5.72</td>
    <td align="right">4.96</td>
    <td align="right">10.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">25.62</td>
    <td align="right">23.56</td>
    <td align="right">23.51</td>
    <td align="right">23.53</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">28.77</td>
    <td align="right">27.23</td>
    <td align="right">27.27</td>
    <td align="right">27.22</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">13.88</td>
    <td align="right">15.25</td>
    <td align="right">10.85</td>
    <td align="right">17.62</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.07</td>
    <td align="right">34.93</td>
    <td align="right">34.97</td>
    <td align="right">35.00</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">39.70</td>
    <td align="right">37.87</td>
    <td align="right">37.90</td>
    <td align="right">37.88</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">16.34</td>
    <td align="right">17.86</td>
    <td align="right">12.37</td>
    <td align="right">19.88</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.13</td>
    <td align="right">4.76</td>
    <td align="right">4.75</td>
    <td align="right">4.74</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.14</td>
    <td align="right">3.52</td>
    <td align="right">3.61</td>
    <td align="right">3.45</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.22</td>
    <td align="right">3.38</td>
    <td align="right">3.40</td>
    <td align="right">3.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">6.53</td>
    <td align="right">6.49</td>
    <td align="right">5.47</td>
    <td align="right">11.52</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">7.15</td>
    <td align="right">7.79</td>
    <td align="right">6.83</td>
    <td align="right">13.32</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">9.42</td>
    <td align="right">8.86</td>
    <td align="right">7.65</td>
    <td align="right">13.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">14.24</td>
    <td align="right">15.23</td>
    <td align="right">10.85</td>
    <td align="right">17.09</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">22.70</td>
    <td align="right">19.00</td>
    <td align="right">16.04</td>
    <td align="right">22.35</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">20.12</td>
    <td align="right">18.39</td>
    <td align="right">15.61</td>
    <td align="right">21.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.77</td>
    <td align="right">17.94</td>
    <td align="right">12.37</td>
    <td align="right">19.83</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">28.63</td>
    <td align="right">26.95</td>
    <td align="right">19.01</td>
    <td align="right">27.11</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">28.67</td>
    <td align="right">26.84</td>
    <td align="right">19.05</td>
    <td align="right">26.25</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">7.70</td>
    <td align="right">7.42</td>
    <td align="right">12.03</td>
    <td align="right">11.54</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">10.62</td>
    <td align="right">9.68</td>
    <td align="right">14.83</td>
    <td align="right">13.85</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">11.60</td>
    <td align="right">10.03</td>
    <td align="right">10.00</td>
    <td align="right">9.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">11.86</td>
    <td align="right">13.20</td>
    <td align="right">14.33</td>
    <td align="right">16.09</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">16.26</td>
    <td align="right">18.50</td>
    <td align="right">17.22</td>
    <td align="right">20.93</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">18.76</td>
    <td align="right">18.96</td>
    <td align="right">18.99</td>
    <td align="right">18.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">24.73</td>
    <td align="right">25.10</td>
    <td align="right">19.58</td>
    <td align="right">26.88</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">33.00</td>
    <td align="right">32.15</td>
    <td align="right">19.91</td>
    <td align="right">32.23</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">40.29</td>
    <td align="right">38.90</td>
    <td align="right">39.08</td>
    <td align="right">39.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">35.43</td>
    <td align="right">34.85</td>
    <td align="right">23.08</td>
    <td align="right">37.09</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">42.59</td>
    <td align="right">41.35</td>
    <td align="right">21.94</td>
    <td align="right">41.81</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">68.81</td>
    <td align="right">64.65</td>
    <td align="right">64.62</td>
    <td align="right">64.79</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">74.09</td>
    <td align="right">34.73</td>
    <td align="right">14.47</td>
    <td align="right">29.71</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">30.98</td>
    <td align="right">44.44</td>
    <td align="right">37.71</td>
    <td align="right">41.10</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">13.31</td>
    <td align="right">16.21</td>
    <td align="right">16.42</td>
    <td align="right">16.21</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">14.61</td>
    <td align="right">18.01</td>
    <td align="right">18.00</td>
    <td align="right">17.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">46.87</td>
    <td align="right">67.42</td>
    <td align="right">40.52</td>
    <td align="right">53.88</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">15.36</td>
    <td align="right">18.48</td>
    <td align="right">18.30</td>
    <td align="right">18.56</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">16.11</td>
    <td align="right">19.08</td>
    <td align="right">19.10</td>
    <td align="right">19.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">57.04</td>
    <td align="right">82.18</td>
    <td align="right">39.01</td>
    <td align="right">61.14</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">16.38</td>
    <td align="right">20.51</td>
    <td align="right">20.45</td>
    <td align="right">20.45</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">16.90</td>
    <td align="right">22.05</td>
    <td align="right">21.17</td>
    <td align="right">21.20</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">72.74</td>
    <td align="right">100.85</td>
    <td align="right">41.16</td>
    <td align="right">72.12</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">17.67</td>
    <td align="right">22.20</td>
    <td align="right">22.27</td>
    <td align="right">22.19</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">19.56</td>
    <td align="right">23.01</td>
    <td align="right">22.98</td>
    <td align="right">23.08</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.89</td>
    <td align="right">23.76</td>
    <td align="right">23.72</td>
    <td align="right">23.73</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.28</td>
    <td align="right">26.54</td>
    <td align="right">26.54</td>
    <td align="right">26.60</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">12.91</td>
    <td align="right">15.55</td>
    <td align="right">15.61</td>
    <td align="right">15.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">27.39</td>
    <td align="right">29.99</td>
    <td align="right">30.06</td>
    <td align="right">30.06</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.06</td>
    <td align="right">34.59</td>
    <td align="right">34.59</td>
    <td align="right">34.59</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">15.28</td>
    <td align="right">17.76</td>
    <td align="right">17.77</td>
    <td align="right">17.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.25</td>
    <td align="right">37.10</td>
    <td align="right">36.89</td>
    <td align="right">36.94</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.62</td>
    <td align="right">49.11</td>
    <td align="right">49.04</td>
    <td align="right">49.02</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">17.01</td>
    <td align="right">20.83</td>
    <td align="right">20.83</td>
    <td align="right">20.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.73</td>
    <td align="right">41.65</td>
    <td align="right">41.70</td>
    <td align="right">41.68</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.44</td>
    <td align="right">58.53</td>
    <td align="right">58.58</td>
    <td align="right">58.52</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">23.83</td>
    <td align="right">26.11</td>
    <td align="right">25.99</td>
    <td align="right">26.04</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">14.47</td>
    <td align="right">16.85</td>
    <td align="right">16.95</td>
    <td align="right">16.81</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.94</td>
    <td align="right">23.76</td>
    <td align="right">23.77</td>
    <td align="right">23.75</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.23</td>
    <td align="right">26.55</td>
    <td align="right">26.55</td>
    <td align="right">26.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">18.97</td>
    <td align="right">21.03</td>
    <td align="right">21.17</td>
    <td align="right">21.05</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.70</td>
    <td align="right">30.00</td>
    <td align="right">29.99</td>
    <td align="right">30.04</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.06</td>
    <td align="right">34.61</td>
    <td align="right">34.61</td>
    <td align="right">34.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">23.43</td>
    <td align="right">25.10</td>
    <td align="right">25.12</td>
    <td align="right">25.21</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.20</td>
    <td align="right">37.12</td>
    <td align="right">36.91</td>
    <td align="right">37.12</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.64</td>
    <td align="right">49.22</td>
    <td align="right">49.11</td>
    <td align="right">49.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">31.64</td>
    <td align="right">33.08</td>
    <td align="right">33.09</td>
    <td align="right">33.32</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.38</td>
    <td align="right">41.71</td>
    <td align="right">41.56</td>
    <td align="right">41.64</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.46</td>
    <td align="right">58.53</td>
    <td align="right">58.56</td>
    <td align="right">58.56</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.32</td>
    <td align="right">24.39</td>
    <td align="right">27.77</td>
    <td align="right">28.20</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">33.73</td>
    <td align="right">31.57</td>
    <td align="right">35.54</td>
    <td align="right">33.52</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">29.70</td>
    <td align="right">34.60</td>
    <td align="right">34.77</td>
    <td align="right">34.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">28.37</td>
    <td align="right">37.02</td>
    <td align="right">28.60</td>
    <td align="right">35.88</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">45.32</td>
    <td align="right">40.87</td>
    <td align="right">34.51</td>
    <td align="right">39.28</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">42.40</td>
    <td align="right">44.78</td>
    <td align="right">44.68</td>
    <td align="right">44.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">37.13</td>
    <td align="right">43.86</td>
    <td align="right">28.00</td>
    <td align="right">39.79</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">49.55</td>
    <td align="right">49.72</td>
    <td align="right">36.11</td>
    <td align="right">44.31</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">44.45</td>
    <td align="right">47.20</td>
    <td align="right">47.04</td>
    <td align="right">47.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">42.27</td>
    <td align="right">49.11</td>
    <td align="right">29.41</td>
    <td align="right">42.72</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">52.33</td>
    <td align="right">52.60</td>
    <td align="right">36.00</td>
    <td align="right">45.96</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">60.46</td>
    <td align="right">65.00</td>
    <td align="right">64.63</td>
    <td align="right">65.65</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">108.11</td>
    <td align="right">126.55</td>
    <td align="right">27.29</td>
    <td align="right">83.53</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">39.06</td>
    <td align="right">53.32</td>
    <td align="right">44.09</td>
    <td align="right">48.83</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">16.97</td>
    <td align="right">20.53</td>
    <td align="right">20.18</td>
    <td align="right">21.04</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">17.21</td>
    <td align="right">20.43</td>
    <td align="right">20.61</td>
    <td align="right">20.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">104.80</td>
    <td align="right">136.59</td>
    <td align="right">61.31</td>
    <td align="right">98.95</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.28</td>
    <td align="right">28.43</td>
    <td align="right">28.07</td>
    <td align="right">28.54</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">23.96</td>
    <td align="right">29.28</td>
    <td align="right">29.34</td>
    <td align="right">29.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">188.87</td>
    <td align="right">244.82</td>
    <td align="right">76.75</td>
    <td align="right">161.61</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">36.76</td>
    <td align="right">46.70</td>
    <td align="right">46.67</td>
    <td align="right">46.70</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">39.90</td>
    <td align="right">50.51</td>
    <td align="right">50.48</td>
    <td align="right">50.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">297.46</td>
    <td align="right">402.05</td>
    <td align="right">98.95</td>
    <td align="right">250.37</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">46.99</td>
    <td align="right">63.80</td>
    <td align="right">63.77</td>
    <td align="right">63.79</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">54.04</td>
    <td align="right">65.21</td>
    <td align="right">65.67</td>
    <td align="right">64.99</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">23.55</td>
    <td align="right">27.71</td>
    <td align="right">27.65</td>
    <td align="right">27.62</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.04</td>
    <td align="right">31.57</td>
    <td align="right">31.71</td>
    <td align="right">31.60</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">14.72</td>
    <td align="right">17.77</td>
    <td align="right">17.75</td>
    <td align="right">17.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">41.09</td>
    <td align="right">44.08</td>
    <td align="right">44.02</td>
    <td align="right">44.02</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">54.32</td>
    <td align="right">48.53</td>
    <td align="right">48.45</td>
    <td align="right">48.42</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">25.55</td>
    <td align="right">26.60</td>
    <td align="right">26.81</td>
    <td align="right">26.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">66.40</td>
    <td align="right">70.90</td>
    <td align="right">70.90</td>
    <td align="right">71.22</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">102.60</td>
    <td align="right">81.99</td>
    <td align="right">82.04</td>
    <td align="right">81.95</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">41.93</td>
    <td align="right">45.04</td>
    <td align="right">46.64</td>
    <td align="right">48.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.31</td>
    <td align="right">92.93</td>
    <td align="right">92.90</td>
    <td align="right">92.62</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.29</td>
    <td align="right">110.10</td>
    <td align="right">110.18</td>
    <td align="right">110.08</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">69.41</td>
    <td align="right">74.63</td>
    <td align="right">74.78</td>
    <td align="right">74.68</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">17.00</td>
    <td align="right">20.30</td>
    <td align="right">20.03</td>
    <td align="right">20.13</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">24.33</td>
    <td align="right">28.61</td>
    <td align="right">28.51</td>
    <td align="right">28.49</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">29.33</td>
    <td align="right">30.66</td>
    <td align="right">30.64</td>
    <td align="right">30.65</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">28.89</td>
    <td align="right">31.57</td>
    <td align="right">30.95</td>
    <td align="right">31.02</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.26</td>
    <td align="right">44.60</td>
    <td align="right">44.51</td>
    <td align="right">44.72</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">53.40</td>
    <td align="right">51.36</td>
    <td align="right">51.29</td>
    <td align="right">51.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">48.53</td>
    <td align="right">56.79</td>
    <td align="right">56.86</td>
    <td align="right">57.83</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.93</td>
    <td align="right">72.42</td>
    <td align="right">72.31</td>
    <td align="right">72.61</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">103.40</td>
    <td align="right">81.23</td>
    <td align="right">81.18</td>
    <td align="right">81.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">81.75</td>
    <td align="right">85.10</td>
    <td align="right">88.90</td>
    <td align="right">92.56</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.20</td>
    <td align="right">99.95</td>
    <td align="right">98.29</td>
    <td align="right">97.07</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">133.74</td>
    <td align="right">110.32</td>
    <td align="right">110.41</td>
    <td align="right">110.39</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">22.14</td>
    <td align="right">29.51</td>
    <td align="right">31.55</td>
    <td align="right">34.04</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">35.81</td>
    <td align="right">36.65</td>
    <td align="right">39.73</td>
    <td align="right">39.24</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">35.94</td>
    <td align="right">40.43</td>
    <td align="right">40.65</td>
    <td align="right">41.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">41.07</td>
    <td align="right">47.01</td>
    <td align="right">36.19</td>
    <td align="right">45.83</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">57.38</td>
    <td align="right">57.49</td>
    <td align="right">44.93</td>
    <td align="right">55.15</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">63.16</td>
    <td align="right">65.24</td>
    <td align="right">65.27</td>
    <td align="right">65.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">65.19</td>
    <td align="right">72.17</td>
    <td align="right">46.66</td>
    <td align="right">67.68</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">87.52</td>
    <td align="right">89.02</td>
    <td align="right">60.63</td>
    <td align="right">80.92</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">90.35</td>
    <td align="right">94.93</td>
    <td align="right">94.94</td>
    <td align="right">94.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">83.66</td>
    <td align="right">90.79</td>
    <td align="right">56.64</td>
    <td align="right">84.30</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">104.61</td>
    <td align="right">104.75</td>
    <td align="right">67.84</td>
    <td align="right">94.38</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">141.07</td>
    <td align="right">140.95</td>
    <td align="right">140.11</td>
    <td align="right">144.32</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">78.84</td>
    <td align="right">14.08</td>
    <td align="right">8.49</td>
    <td align="right">17.91</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">21.41</td>
    <td align="right">28.24</td>
    <td align="right">29.12</td>
    <td align="right">29.00</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">12.43</td>
    <td align="right">13.90</td>
    <td align="right">13.90</td>
    <td align="right">13.88</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">15.76</td>
    <td align="right">17.93</td>
    <td align="right">17.93</td>
    <td align="right">17.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">31.41</td>
    <td align="right">42.27</td>
    <td align="right">31.24</td>
    <td align="right">37.90</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">16.04</td>
    <td align="right">18.35</td>
    <td align="right">18.35</td>
    <td align="right">18.41</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">18.19</td>
    <td align="right">20.68</td>
    <td align="right">20.69</td>
    <td align="right">20.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">39.27</td>
    <td align="right">64.39</td>
    <td align="right">32.88</td>
    <td align="right">52.76</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">18.58</td>
    <td align="right">21.19</td>
    <td align="right">21.36</td>
    <td align="right">21.19</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">22.04</td>
    <td align="right">22.89</td>
    <td align="right">22.92</td>
    <td align="right">22.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">63.21</td>
    <td align="right">81.81</td>
    <td align="right">32.81</td>
    <td align="right">56.65</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">22.18</td>
    <td align="right">23.25</td>
    <td align="right">23.25</td>
    <td align="right">23.25</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">24.04</td>
    <td align="right">25.69</td>
    <td align="right">25.68</td>
    <td align="right">25.64</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.02</td>
    <td align="right">18.29</td>
    <td align="right">18.41</td>
    <td align="right">18.38</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.04</td>
    <td align="right">18.84</td>
    <td align="right">18.84</td>
    <td align="right">18.82</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">7.96</td>
    <td align="right">8.72</td>
    <td align="right">8.72</td>
    <td align="right">8.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.69</td>
    <td align="right">26.53</td>
    <td align="right">26.56</td>
    <td align="right">26.58</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.57</td>
    <td align="right">26.92</td>
    <td align="right">26.90</td>
    <td align="right">26.91</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">11.93</td>
    <td align="right">13.75</td>
    <td align="right">13.76</td>
    <td align="right">13.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.19</td>
    <td align="right">35.30</td>
    <td align="right">35.34</td>
    <td align="right">35.28</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.54</td>
    <td align="right">34.08</td>
    <td align="right">34.38</td>
    <td align="right">34.16</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">13.85</td>
    <td align="right">17.79</td>
    <td align="right">17.80</td>
    <td align="right">17.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.55</td>
    <td align="right">38.24</td>
    <td align="right">38.25</td>
    <td align="right">38.29</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.38</td>
    <td align="right">41.01</td>
    <td align="right">40.99</td>
    <td align="right">41.19</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">19.12</td>
    <td align="right">19.77</td>
    <td align="right">19.71</td>
    <td align="right">19.73</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">7.68</td>
    <td align="right">8.71</td>
    <td align="right">8.48</td>
    <td align="right">8.48</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.02</td>
    <td align="right">18.45</td>
    <td align="right">18.32</td>
    <td align="right">18.42</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.06</td>
    <td align="right">18.86</td>
    <td align="right">18.87</td>
    <td align="right">18.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">11.91</td>
    <td align="right">14.08</td>
    <td align="right">14.10</td>
    <td align="right">14.07</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.67</td>
    <td align="right">26.55</td>
    <td align="right">26.56</td>
    <td align="right">26.58</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.55</td>
    <td align="right">26.92</td>
    <td align="right">26.92</td>
    <td align="right">26.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">14.20</td>
    <td align="right">17.22</td>
    <td align="right">17.22</td>
    <td align="right">17.21</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.14</td>
    <td align="right">35.25</td>
    <td align="right">35.23</td>
    <td align="right">35.29</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.56</td>
    <td align="right">34.18</td>
    <td align="right">34.12</td>
    <td align="right">34.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">18.80</td>
    <td align="right">19.99</td>
    <td align="right">19.99</td>
    <td align="right">19.97</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.55</td>
    <td align="right">38.23</td>
    <td align="right">38.26</td>
    <td align="right">38.26</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.48</td>
    <td align="right">41.02</td>
    <td align="right">41.03</td>
    <td align="right">41.25</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.26</td>
    <td align="right">20.94</td>
    <td align="right">24.72</td>
    <td align="right">25.07</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">47.95</td>
    <td align="right">41.99</td>
    <td align="right">41.73</td>
    <td align="right">41.48</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">27.54</td>
    <td align="right">27.19</td>
    <td align="right">27.13</td>
    <td align="right">27.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">26.98</td>
    <td align="right">29.74</td>
    <td align="right">24.26</td>
    <td align="right">29.79</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">53.10</td>
    <td align="right">46.80</td>
    <td align="right">40.18</td>
    <td align="right">43.43</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">37.03</td>
    <td align="right">36.99</td>
    <td align="right">36.94</td>
    <td align="right">36.70</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">33.14</td>
    <td align="right">35.80</td>
    <td align="right">24.46</td>
    <td align="right">33.80</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">60.38</td>
    <td align="right">53.86</td>
    <td align="right">40.39</td>
    <td align="right">47.28</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">39.67</td>
    <td align="right">38.71</td>
    <td align="right">38.84</td>
    <td align="right">38.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">39.75</td>
    <td align="right">46.72</td>
    <td align="right">30.13</td>
    <td align="right">41.50</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">62.68</td>
    <td align="right">58.92</td>
    <td align="right">44.52</td>
    <td align="right">51.73</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">51.96</td>
    <td align="right">50.19</td>
    <td align="right">50.65</td>
    <td align="right">50.16</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">123.91</td>
    <td align="right">61.87</td>
    <td align="right">23.10</td>
    <td align="right">53.24</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">36.20</td>
    <td align="right">44.92</td>
    <td align="right">37.30</td>
    <td align="right">41.59</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">13.51</td>
    <td align="right">15.03</td>
    <td align="right">15.13</td>
    <td align="right">14.96</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">19.56</td>
    <td align="right">21.57</td>
    <td align="right">21.53</td>
    <td align="right">21.67</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">73.72</td>
    <td align="right">91.77</td>
    <td align="right">45.71</td>
    <td align="right">69.46</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">26.60</td>
    <td align="right">29.00</td>
    <td align="right">29.02</td>
    <td align="right">29.21</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">29.41</td>
    <td align="right">34.58</td>
    <td align="right">34.72</td>
    <td align="right">34.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">144.58</td>
    <td align="right">204.41</td>
    <td align="right">67.54</td>
    <td align="right">139.63</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">40.05</td>
    <td align="right">47.86</td>
    <td align="right">47.74</td>
    <td align="right">47.84</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">52.06</td>
    <td align="right">50.68</td>
    <td align="right">50.70</td>
    <td align="right">50.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">249.06</td>
    <td align="right">300.74</td>
    <td align="right">82.61</td>
    <td align="right">195.14</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">63.86</td>
    <td align="right">63.18</td>
    <td align="right">63.16</td>
    <td align="right">63.11</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">67.48</td>
    <td align="right">67.20</td>
    <td align="right">67.20</td>
    <td align="right">67.09</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">21.20</td>
    <td align="right">22.72</td>
    <td align="right">22.68</td>
    <td align="right">22.59</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">19.92</td>
    <td align="right">22.76</td>
    <td align="right">22.68</td>
    <td align="right">22.79</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">10.85</td>
    <td align="right">11.61</td>
    <td align="right">11.82</td>
    <td align="right">11.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">33.42</td>
    <td align="right">38.69</td>
    <td align="right">38.57</td>
    <td align="right">38.86</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">43.31</td>
    <td align="right">44.74</td>
    <td align="right">44.82</td>
    <td align="right">44.95</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">21.67</td>
    <td align="right">21.87</td>
    <td align="right">21.68</td>
    <td align="right">21.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.25</td>
    <td align="right">69.48</td>
    <td align="right">69.40</td>
    <td align="right">69.29</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">70.69</td>
    <td align="right">68.64</td>
    <td align="right">68.50</td>
    <td align="right">68.64</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">38.08</td>
    <td align="right">42.26</td>
    <td align="right">42.08</td>
    <td align="right">41.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.06</td>
    <td align="right">86.29</td>
    <td align="right">86.26</td>
    <td align="right">86.29</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.69</td>
    <td align="right">91.61</td>
    <td align="right">91.46</td>
    <td align="right">91.55</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">53.07</td>
    <td align="right">52.45</td>
    <td align="right">52.20</td>
    <td align="right">52.54</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">8.58</td>
    <td align="right">9.76</td>
    <td align="right">10.06</td>
    <td align="right">9.65</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">20.03</td>
    <td align="right">21.67</td>
    <td align="right">21.35</td>
    <td align="right">21.48</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.06</td>
    <td align="right">22.61</td>
    <td align="right">22.82</td>
    <td align="right">22.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">22.40</td>
    <td align="right">23.01</td>
    <td align="right">22.86</td>
    <td align="right">22.90</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">37.19</td>
    <td align="right">39.26</td>
    <td align="right">39.28</td>
    <td align="right">39.41</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">44.39</td>
    <td align="right">41.85</td>
    <td align="right">41.71</td>
    <td align="right">41.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">37.58</td>
    <td align="right">40.61</td>
    <td align="right">40.50</td>
    <td align="right">40.45</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">66.18</td>
    <td align="right">67.87</td>
    <td align="right">67.91</td>
    <td align="right">68.20</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">69.58</td>
    <td align="right">68.00</td>
    <td align="right">67.93</td>
    <td align="right">68.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">53.02</td>
    <td align="right">53.59</td>
    <td align="right">53.59</td>
    <td align="right">53.66</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.59</td>
    <td align="right">89.06</td>
    <td align="right">89.09</td>
    <td align="right">89.63</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.31</td>
    <td align="right">93.20</td>
    <td align="right">93.04</td>
    <td align="right">93.22</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">21.39</td>
    <td align="right">24.87</td>
    <td align="right">27.37</td>
    <td align="right">30.44</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">50.00</td>
    <td align="right">43.76</td>
    <td align="right">43.91</td>
    <td align="right">45.10</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">31.82</td>
    <td align="right">30.58</td>
    <td align="right">30.66</td>
    <td align="right">30.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">40.61</td>
    <td align="right">43.85</td>
    <td align="right">32.01</td>
    <td align="right">43.66</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">64.29</td>
    <td align="right">59.25</td>
    <td align="right">50.29</td>
    <td align="right">57.43</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">57.89</td>
    <td align="right">51.37</td>
    <td align="right">51.20</td>
    <td align="right">51.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">62.05</td>
    <td align="right">63.50</td>
    <td align="right">40.19</td>
    <td align="right">60.84</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">89.16</td>
    <td align="right">86.74</td>
    <td align="right">63.32</td>
    <td align="right">78.81</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">86.57</td>
    <td align="right">79.35</td>
    <td align="right">79.28</td>
    <td align="right">79.40</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">81.80</td>
    <td align="right">89.22</td>
    <td align="right">57.41</td>
    <td align="right">83.74</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">108.60</td>
    <td align="right">106.74</td>
    <td align="right">79.29</td>
    <td align="right">96.78</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">131.64</td>
    <td align="right">115.54</td>
    <td align="right">115.95</td>
    <td align="right">115.71</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">33.46</td>
    <td align="right">6.65</td>
    <td align="right">5.64</td>
    <td align="right">12.26</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">65.48</td>
    <td align="right">60.56</td>
    <td align="right">39.69</td>
    <td align="right">50.14</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">20.99</td>
    <td align="right">20.58</td>
    <td align="right">22.73</td>
    <td align="right">25.28</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">25.02</td>
    <td align="right">24.72</td>
    <td align="right">26.40</td>
    <td align="right">27.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">99.93</td>
    <td align="right">87.74</td>
    <td align="right">42.30</td>
    <td align="right">63.39</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">22.54</td>
    <td align="right">27.12</td>
    <td align="right">26.77</td>
    <td align="right">29.00</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">27.67</td>
    <td align="right">27.87</td>
    <td align="right">28.61</td>
    <td align="right">30.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">130.89</td>
    <td align="right">105.49</td>
    <td align="right">39.74</td>
    <td align="right">73.35</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">31.38</td>
    <td align="right">25.83</td>
    <td align="right">25.97</td>
    <td align="right">28.95</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">33.20</td>
    <td align="right">44.44</td>
    <td align="right">43.98</td>
    <td align="right">46.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">158.19</td>
    <td align="right">135.90</td>
    <td align="right">41.66</td>
    <td align="right">88.07</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">36.34</td>
    <td align="right">26.86</td>
    <td align="right">27.27</td>
    <td align="right">30.48</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">38.41</td>
    <td align="right">31.97</td>
    <td align="right">32.36</td>
    <td align="right">36.26</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">24.31</td>
    <td align="right">41.49</td>
    <td align="right">41.39</td>
    <td align="right">41.44</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.41</td>
    <td align="right">41.19</td>
    <td align="right">41.11</td>
    <td align="right">41.27</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">17.71</td>
    <td align="right">28.44</td>
    <td align="right">28.38</td>
    <td align="right">28.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">29.68</td>
    <td align="right">56.24</td>
    <td align="right">56.18</td>
    <td align="right">55.67</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">32.20</td>
    <td align="right">56.07</td>
    <td align="right">56.46</td>
    <td align="right">57.76</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">16.82</td>
    <td align="right">37.46</td>
    <td align="right">27.81</td>
    <td align="right">37.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">43.49</td>
    <td align="right">77.27</td>
    <td align="right">77.50</td>
    <td align="right">77.05</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">47.28</td>
    <td align="right">77.35</td>
    <td align="right">77.56</td>
    <td align="right">77.47</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">33.17</td>
    <td align="right">75.43</td>
    <td align="right">60.26</td>
    <td align="right">71.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">55.57</td>
    <td align="right">83.25</td>
    <td align="right">85.07</td>
    <td align="right">83.38</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">57.97</td>
    <td align="right">89.85</td>
    <td align="right">88.77</td>
    <td align="right">88.64</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">27.15</td>
    <td align="right">54.00</td>
    <td align="right">37.28</td>
    <td align="right">50.49</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4745</td>
    <td align="right">17.95</td>
    <td align="right">28.22</td>
    <td align="right">28.00</td>
    <td align="right">27.62</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.81</td>
    <td align="right">30.65</td>
    <td align="right">30.20</td>
    <td align="right">30.22</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">20.39</td>
    <td align="right">30.74</td>
    <td align="right">30.74</td>
    <td align="right">30.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">18.02</td>
    <td align="right">44.38</td>
    <td align="right">34.92</td>
    <td align="right">44.47</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">18.83</td>
    <td align="right">38.67</td>
    <td align="right">28.97</td>
    <td align="right">38.50</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">20.71</td>
    <td align="right">46.40</td>
    <td align="right">36.96</td>
    <td align="right">46.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">34.15</td>
    <td align="right">71.80</td>
    <td align="right">55.02</td>
    <td align="right">69.08</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">37.11</td>
    <td align="right">57.76</td>
    <td align="right">39.76</td>
    <td align="right">53.46</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">36.39</td>
    <td align="right">56.94</td>
    <td align="right">39.43</td>
    <td align="right">53.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">33.96</td>
    <td align="right">53.81</td>
    <td align="right">36.80</td>
    <td align="right">50.15</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">38.12</td>
    <td align="right">59.45</td>
    <td align="right">40.13</td>
    <td align="right">54.63</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">34.58</td>
    <td align="right">58.74</td>
    <td align="right">39.78</td>
    <td align="right">54.14</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">27.01</td>
    <td align="right">43.65</td>
    <td align="right">32.85</td>
    <td align="right">39.10</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">33.00</td>
    <td align="right">56.15</td>
    <td align="right">36.89</td>
    <td align="right">46.25</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">36.41</td>
    <td align="right">60.79</td>
    <td align="right">60.81</td>
    <td align="right">60.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">35.60</td>
    <td align="right">61.94</td>
    <td align="right">33.10</td>
    <td align="right">48.16</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">40.04</td>
    <td align="right">62.49</td>
    <td align="right">35.66</td>
    <td align="right">49.59</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">44.85</td>
    <td align="right">77.67</td>
    <td align="right">77.74</td>
    <td align="right">77.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">40.89</td>
    <td align="right">74.07</td>
    <td align="right">33.54</td>
    <td align="right">54.74</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">52.06</td>
    <td align="right">95.88</td>
    <td align="right">55.57</td>
    <td align="right">77.01</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">57.66</td>
    <td align="right">85.11</td>
    <td align="right">85.09</td>
    <td align="right">84.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">56.72</td>
    <td align="right">99.50</td>
    <td align="right">34.94</td>
    <td align="right">69.26</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">71.17</td>
    <td align="right">99.23</td>
    <td align="right">36.85</td>
    <td align="right">69.33</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">73.28</td>
    <td align="right">116.90</td>
    <td align="right">117.07</td>
    <td align="right">116.97</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">64.08</td>
    <td align="right">34.02</td>
    <td align="right">20.61</td>
    <td align="right">37.98</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">71.81</td>
    <td align="right">61.92</td>
    <td align="right">41.28</td>
    <td align="right">51.96</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">25.87</td>
    <td align="right">20.72</td>
    <td align="right">23.29</td>
    <td align="right">26.24</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">38.05</td>
    <td align="right">26.88</td>
    <td align="right">28.29</td>
    <td align="right">29.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">154.39</td>
    <td align="right">146.45</td>
    <td align="right">58.10</td>
    <td align="right">102.20</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">26.71</td>
    <td align="right">37.91</td>
    <td align="right">39.71</td>
    <td align="right">42.99</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">38.31</td>
    <td align="right">30.74</td>
    <td align="right">31.24</td>
    <td align="right">33.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">275.30</td>
    <td align="right">232.55</td>
    <td align="right">65.49</td>
    <td align="right">152.30</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">40.14</td>
    <td align="right">40.04</td>
    <td align="right">40.68</td>
    <td align="right">44.59</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">70.01</td>
    <td align="right">71.35</td>
    <td align="right">70.15</td>
    <td align="right">73.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">444.85</td>
    <td align="right">359.29</td>
    <td align="right">80.33</td>
    <td align="right">223.01</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">45.38</td>
    <td align="right">44.77</td>
    <td align="right">46.00</td>
    <td align="right">50.34</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">62.74</td>
    <td align="right">63.76</td>
    <td align="right">64.01</td>
    <td align="right">67.04</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">36.49</td>
    <td align="right">49.51</td>
    <td align="right">49.57</td>
    <td align="right">49.36</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">29.99</td>
    <td align="right">41.49</td>
    <td align="right">41.30</td>
    <td align="right">41.51</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">20.43</td>
    <td align="right">30.39</td>
    <td align="right">30.37</td>
    <td align="right">30.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">45.87</td>
    <td align="right">73.27</td>
    <td align="right">73.51</td>
    <td align="right">73.02</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">49.27</td>
    <td align="right">76.70</td>
    <td align="right">76.99</td>
    <td align="right">78.12</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">38.35</td>
    <td align="right">67.42</td>
    <td align="right">58.85</td>
    <td align="right">67.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">59.52</td>
    <td align="right">91.61</td>
    <td align="right">91.55</td>
    <td align="right">91.60</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">66.28</td>
    <td align="right">95.39</td>
    <td align="right">95.20</td>
    <td align="right">95.23</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">49.13</td>
    <td align="right">79.96</td>
    <td align="right">62.98</td>
    <td align="right">76.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">74.52</td>
    <td align="right">106.41</td>
    <td align="right">107.48</td>
    <td align="right">106.45</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">84.88</td>
    <td align="right">118.73</td>
    <td align="right">118.03</td>
    <td align="right">117.98</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">58.98</td>
    <td align="right">89.87</td>
    <td align="right">73.74</td>
    <td align="right">86.51</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4716</td>
    <td align="right">23.87</td>
    <td align="right">29.98</td>
    <td align="right">29.99</td>
    <td align="right">29.95</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">40.19</td>
    <td align="right">86.12</td>
    <td align="right">86.15</td>
    <td align="right">86.24</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">20.80</td>
    <td align="right">31.91</td>
    <td align="right">31.97</td>
    <td align="right">31.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">27.70</td>
    <td align="right">51.48</td>
    <td align="right">41.87</td>
    <td align="right">51.88</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">23.90</td>
    <td align="right">42.21</td>
    <td align="right">32.28</td>
    <td align="right">42.12</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">23.61</td>
    <td align="right">60.26</td>
    <td align="right">51.07</td>
    <td align="right">61.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">50.55</td>
    <td align="right">80.15</td>
    <td align="right">63.58</td>
    <td align="right">77.32</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">52.55</td>
    <td align="right">81.06</td>
    <td align="right">63.43</td>
    <td align="right">77.45</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">53.73</td>
    <td align="right">82.02</td>
    <td align="right">63.87</td>
    <td align="right">77.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">60.69</td>
    <td align="right">90.82</td>
    <td align="right">73.94</td>
    <td align="right">87.89</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">62.34</td>
    <td align="right">96.13</td>
    <td align="right">76.20</td>
    <td align="right">91.24</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">63.54</td>
    <td align="right">96.28</td>
    <td align="right">76.08</td>
    <td align="right">91.31</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">37.28</td>
    <td align="right">61.71</td>
    <td align="right">56.29</td>
    <td align="right">60.32</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">47.15</td>
    <td align="right">64.66</td>
    <td align="right">48.41</td>
    <td align="right">56.50</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">48.66</td>
    <td align="right">74.54</td>
    <td align="right">74.61</td>
    <td align="right">74.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">50.33</td>
    <td align="right">64.56</td>
    <td align="right">36.71</td>
    <td align="right">51.22</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">49.99</td>
    <td align="right">67.46</td>
    <td align="right">41.35</td>
    <td align="right">55.03</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">85.35</td>
    <td align="right">108.29</td>
    <td align="right">108.13</td>
    <td align="right">108.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">62.14</td>
    <td align="right">89.19</td>
    <td align="right">52.95</td>
    <td align="right">72.04</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">73.32</td>
    <td align="right">102.44</td>
    <td align="right">62.21</td>
    <td align="right">82.69</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">77.96</td>
    <td align="right">105.06</td>
    <td align="right">105.01</td>
    <td align="right">104.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">81.08</td>
    <td align="right">122.18</td>
    <td align="right">64.08</td>
    <td align="right">94.89</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">92.69</td>
    <td align="right">130.90</td>
    <td align="right">72.61</td>
    <td align="right">103.02</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">104.87</td>
    <td align="right">143.38</td>
    <td align="right">143.53</td>
    <td align="right">143.41</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
