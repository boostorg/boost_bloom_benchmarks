# Experimental results for [candidate Boost Bloom Library](https://github.com/joaquintides/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for nine different configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-mavx2`),
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
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.94</td>
    <td align="right">4.59</td>
    <td align="right">3.63</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">11.39</td>
    <td align="right">10.73</td>
    <td align="right">16.69</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">4.04</td>
    <td align="right">4.37</td>
    <td align="right">4.37</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.93</td>
    <td align="right">5.11</td>
    <td align="right">5.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">17.11</td>
    <td align="right">15.60</td>
    <td align="right">17.49</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.88</td>
    <td align="right">5.00</td>
    <td align="right">5.03</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.44</td>
    <td align="right">5.51</td>
    <td align="right">5.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">20.06</td>
    <td align="right">18.85</td>
    <td align="right">16.55</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.44</td>
    <td align="right">5.40</td>
    <td align="right">5.38</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.32</td>
    <td align="right">6.42</td>
    <td align="right">6.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">26.53</td>
    <td align="right">23.46</td>
    <td align="right">16.89</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.47</td>
    <td align="right">6.17</td>
    <td align="right">5.98</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.80</td>
    <td align="right">6.67</td>
    <td align="right">6.69</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.15</td>
    <td align="right">5.80</td>
    <td align="right">5.81</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.60</td>
    <td align="right">6.74</td>
    <td align="right">6.99</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.00</td>
    <td align="right">3.33</td>
    <td align="right">3.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.09</td>
    <td align="right">8.92</td>
    <td align="right">8.92</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.29</td>
    <td align="right">10.13</td>
    <td align="right">10.17</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.52</td>
    <td align="right">3.15</td>
    <td align="right">3.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">9.39</td>
    <td align="right">13.82</td>
    <td align="right">13.94</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.69</td>
    <td align="right">14.22</td>
    <td align="right">14.25</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.79</td>
    <td align="right">5.91</td>
    <td align="right">3.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">11.23</td>
    <td align="right">15.56</td>
    <td align="right">15.48</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">12.17</td>
    <td align="right">17.47</td>
    <td align="right">17.47</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.91</td>
    <td align="right">5.89</td>
    <td align="right">3.94</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">3.00</td>
    <td align="right">3.30</td>
    <td align="right">3.28</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.44</td>
    <td align="right">5.15</td>
    <td align="right">5.11</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.58</td>
    <td align="right">5.01</td>
    <td align="right">5.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.10</td>
    <td align="right">3.36</td>
    <td align="right">3.37</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.26</td>
    <td align="right">4.51</td>
    <td align="right">4.52</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.52</td>
    <td align="right">5.20</td>
    <td align="right">5.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.47</td>
    <td align="right">5.59</td>
    <td align="right">3.81</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.10</td>
    <td align="right">7.81</td>
    <td align="right">5.91</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">7.92</td>
    <td align="right">7.62</td>
    <td align="right">5.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.51</td>
    <td align="right">5.61</td>
    <td align="right">3.80</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">8.07</td>
    <td align="right">9.19</td>
    <td align="right">5.98</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.40</td>
    <td align="right">9.16</td>
    <td align="right">5.93</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1818</td>
    <td align="right">10.82</td>
    <td align="right">11.17</td>
    <td align="right">17.06</td>
    <td align="center">4</td>
    <td align="right">3.3670</td>
    <td align="right">3.88</td>
    <td align="right">4.46</td>
    <td align="right">4.46</td>
    <td align="center">5</td>
    <td align="right">3.0480</td>
    <td align="right">4.67</td>
    <td align="right">5.31</td>
    <td align="right">5.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3131</td>
    <td align="right">15.99</td>
    <td align="right">16.15</td>
    <td align="right">17.93</td>
    <td align="center">5</td>
    <td align="right">1.0454</td>
    <td align="right">4.47</td>
    <td align="right">5.32</td>
    <td align="right">5.32</td>
    <td align="center">6</td>
    <td align="right">0.8156</td>
    <td align="right">5.38</td>
    <td align="right">5.86</td>
    <td align="right">5.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0462</td>
    <td align="right">18.67</td>
    <td align="right">19.48</td>
    <td align="right">17.16</td>
    <td align="center">6</td>
    <td align="right">0.4073</td>
    <td align="right">5.04</td>
    <td align="right">5.71</td>
    <td align="right">5.67</td>
    <td align="center">7</td>
    <td align="right">0.2848</td>
    <td align="right">5.75</td>
    <td align="right">6.50</td>
    <td align="right">6.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">23.69</td>
    <td align="right">24.75</td>
    <td align="right">17.23</td>
    <td align="center">7</td>
    <td align="right">0.1956</td>
    <td align="right">5.42</td>
    <td align="right">6.39</td>
    <td align="right">6.40</td>
    <td align="center">8</td>
    <td align="right">0.1228</td>
    <td align="right">6.32</td>
    <td align="right">6.93</td>
    <td align="right">6.94</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">4.88</td>
    <td align="right">5.95</td>
    <td align="right">5.93</td>
    <td align="center">5</td>
    <td align="right">2.3163</td>
    <td align="right">5.76</td>
    <td align="right">6.84</td>
    <td align="right">6.86</td>
    <td align="center">5</td>
    <td align="right">2.7392</td>
    <td align="right">3.12</td>
    <td align="right">2.97</td>
    <td align="right">3.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4226</td>
    <td align="right">6.26</td>
    <td align="right">9.13</td>
    <td align="right">8.36</td>
    <td align="center">8</td>
    <td align="right">0.3730</td>
    <td align="right">7.47</td>
    <td align="right">10.02</td>
    <td align="right">10.04</td>
    <td align="center">8</td>
    <td align="right">0.5386</td>
    <td align="right">2.51</td>
    <td align="right">2.75</td>
    <td align="right">2.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0752</td>
    <td align="right">9.19</td>
    <td align="right">13.06</td>
    <td align="right">13.04</td>
    <td align="center">11</td>
    <td align="right">0.0634</td>
    <td align="right">16.87</td>
    <td align="right">14.74</td>
    <td align="right">14.69</td>
    <td align="center">11</td>
    <td align="right">0.1201</td>
    <td align="right">5.79</td>
    <td align="right">6.09</td>
    <td align="right">4.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0135</td>
    <td align="right">11.31</td>
    <td align="right">15.05</td>
    <td align="right">15.04</td>
    <td align="center">14</td>
    <td align="right">0.0146</td>
    <td align="right">12.44</td>
    <td align="right">17.61</td>
    <td align="right">17.58</td>
    <td align="center">13</td>
    <td align="right">0.0319</td>
    <td align="right">5.82</td>
    <td align="right">6.09</td>
    <td align="right">4.07</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4739</td>
    <td align="right">3.15</td>
    <td align="right">2.81</td>
    <td align="right">2.81</td>
    <td align="center">5</td>
    <td align="right">2.4715</td>
    <td align="right">4.58</td>
    <td align="right">4.80</td>
    <td align="right">4.82</td>
    <td align="center">5</td>
    <td align="right">2.3106</td>
    <td align="right">4.56</td>
    <td align="right">4.68</td>
    <td align="right">4.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4474</td>
    <td align="right">3.27</td>
    <td align="right">2.87</td>
    <td align="right">2.88</td>
    <td align="center">8</td>
    <td align="right">0.4256</td>
    <td align="right">3.32</td>
    <td align="right">4.07</td>
    <td align="right">4.08</td>
    <td align="center">8</td>
    <td align="right">0.3856</td>
    <td align="right">4.64</td>
    <td align="right">4.83</td>
    <td align="right">4.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0914</td>
    <td align="right">5.41</td>
    <td align="right">5.77</td>
    <td align="right">3.89</td>
    <td align="center">11</td>
    <td align="right">0.0757</td>
    <td align="right">7.56</td>
    <td align="right">8.03</td>
    <td align="right">6.17</td>
    <td align="center">11</td>
    <td align="right">0.0638</td>
    <td align="right">7.92</td>
    <td align="right">7.74</td>
    <td align="right">5.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0191</td>
    <td align="right">5.44</td>
    <td align="right">5.77</td>
    <td align="right">3.88</td>
    <td align="center">13</td>
    <td align="right">0.0145</td>
    <td align="right">8.16</td>
    <td align="right">9.39</td>
    <td align="right">6.14</td>
    <td align="center">14</td>
    <td align="right">0.0125</td>
    <td align="right">8.53</td>
    <td align="right">9.17</td>
    <td align="right">5.96</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">33.44</td>
    <td align="right">19.77</td>
    <td align="right">8.09</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">11.57</td>
    <td align="right">10.83</td>
    <td align="right">16.72</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.22</td>
    <td align="right">4.43</td>
    <td align="right">4.44</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.11</td>
    <td align="right">5.25</td>
    <td align="right">5.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">16.87</td>
    <td align="right">15.92</td>
    <td align="right">17.47</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">4.84</td>
    <td align="right">4.84</td>
    <td align="right">4.93</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.56</td>
    <td align="right">5.55</td>
    <td align="right">5.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">24.82</td>
    <td align="right">20.95</td>
    <td align="right">17.66</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">9.53</td>
    <td align="right">8.36</td>
    <td align="right">7.13</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">7.40</td>
    <td align="right">6.97</td>
    <td align="right">7.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">41.94</td>
    <td align="right">82.11</td>
    <td align="right">24.23</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">17.11</td>
    <td align="right">18.61</td>
    <td align="right">20.69</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">23.97</td>
    <td align="right">20.70</td>
    <td align="right">20.61</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">5.30</td>
    <td align="right">5.99</td>
    <td align="right">6.00</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">5.77</td>
    <td align="right">6.97</td>
    <td align="right">7.22</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.11</td>
    <td align="right">3.39</td>
    <td align="right">3.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.32</td>
    <td align="right">10.17</td>
    <td align="right">10.69</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">10.22</td>
    <td align="right">12.01</td>
    <td align="right">11.71</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.78</td>
    <td align="right">3.68</td>
    <td align="right">3.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">12.46</td>
    <td align="right">18.04</td>
    <td align="right">17.35</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">25.34</td>
    <td align="right">18.79</td>
    <td align="right">18.88</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">13.30</td>
    <td align="right">12.15</td>
    <td align="right">7.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">24.60</td>
    <td align="right">28.52</td>
    <td align="right">27.20</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">28.69</td>
    <td align="right">35.85</td>
    <td align="right">35.84</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">18.05</td>
    <td align="right">18.34</td>
    <td align="right">12.12</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.08</td>
    <td align="right">3.32</td>
    <td align="right">3.33</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.64</td>
    <td align="right">5.27</td>
    <td align="right">5.18</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.75</td>
    <td align="right">5.06</td>
    <td align="right">5.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.23</td>
    <td align="right">3.46</td>
    <td align="right">3.42</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.51</td>
    <td align="right">4.90</td>
    <td align="right">4.79</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">4.63</td>
    <td align="right">5.26</td>
    <td align="right">5.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">10.50</td>
    <td align="right">12.99</td>
    <td align="right">6.14</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">9.06</td>
    <td align="right">11.69</td>
    <td align="right">6.75</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">9.26</td>
    <td align="right">9.72</td>
    <td align="right">6.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">13.65</td>
    <td align="right">15.57</td>
    <td align="right">9.27</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">15.13</td>
    <td align="right">24.42</td>
    <td align="right">12.50</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">17.49</td>
    <td align="right">22.30</td>
    <td align="right">12.88</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1556</td>
    <td align="right">11.25</td>
    <td align="right">11.14</td>
    <td align="right">17.05</td>
    <td align="center">4</td>
    <td align="right">3.3474</td>
    <td align="right">3.91</td>
    <td align="right">4.44</td>
    <td align="right">4.46</td>
    <td align="center">5</td>
    <td align="right">3.0451</td>
    <td align="right">4.75</td>
    <td align="right">5.38</td>
    <td align="right">5.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3152</td>
    <td align="right">16.12</td>
    <td align="right">15.77</td>
    <td align="right">17.71</td>
    <td align="center">5</td>
    <td align="right">1.0335</td>
    <td align="right">4.51</td>
    <td align="right">5.38</td>
    <td align="right">5.48</td>
    <td align="center">6</td>
    <td align="right">0.8296</td>
    <td align="right">5.34</td>
    <td align="right">5.86</td>
    <td align="right">5.72</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0452</td>
    <td align="right">25.83</td>
    <td align="right">25.66</td>
    <td align="right">18.59</td>
    <td align="center">6</td>
    <td align="right">0.4069</td>
    <td align="right">9.50</td>
    <td align="right">8.70</td>
    <td align="right">8.76</td>
    <td align="center">7</td>
    <td align="right">0.2911</td>
    <td align="right">6.98</td>
    <td align="right">8.64</td>
    <td align="right">8.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">81.22</td>
    <td align="right">78.26</td>
    <td align="right">24.45</td>
    <td align="center">7</td>
    <td align="right">0.1900</td>
    <td align="right">15.89</td>
    <td align="right">17.21</td>
    <td align="right">19.64</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">16.94</td>
    <td align="right">15.67</td>
    <td align="right">13.03</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4408</td>
    <td align="right">5.00</td>
    <td align="right">6.09</td>
    <td align="right">6.12</td>
    <td align="center">5</td>
    <td align="right">2.3114</td>
    <td align="right">5.94</td>
    <td align="right">6.95</td>
    <td align="right">6.97</td>
    <td align="center">5</td>
    <td align="right">2.7422</td>
    <td align="right">3.20</td>
    <td align="right">3.00</td>
    <td align="right">3.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4214</td>
    <td align="right">6.19</td>
    <td align="right">10.00</td>
    <td align="right">9.21</td>
    <td align="center">8</td>
    <td align="right">0.3763</td>
    <td align="right">8.01</td>
    <td align="right">11.40</td>
    <td align="right">11.47</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">2.75</td>
    <td align="right">3.11</td>
    <td align="right">2.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0760</td>
    <td align="right">11.55</td>
    <td align="right">14.13</td>
    <td align="right">13.51</td>
    <td align="center">11</td>
    <td align="right">0.0633</td>
    <td align="right">17.85</td>
    <td align="right">14.88</td>
    <td align="right">14.89</td>
    <td align="center">11</td>
    <td align="right">0.1206</td>
    <td align="right">5.72</td>
    <td align="right">5.85</td>
    <td align="right">3.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0156</td>
    <td align="right">11.44</td>
    <td align="right">14.46</td>
    <td align="right">14.28</td>
    <td align="center">14</td>
    <td align="right">0.0111</td>
    <td align="right">12.98</td>
    <td align="right">17.44</td>
    <td align="right">17.79</td>
    <td align="center">13</td>
    <td align="right">0.0282</td>
    <td align="right">14.91</td>
    <td align="right">14.61</td>
    <td align="right">10.04</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4684</td>
    <td align="right">3.22</td>
    <td align="right">2.87</td>
    <td align="right">2.87</td>
    <td align="center">5</td>
    <td align="right">2.4638</td>
    <td align="right">4.77</td>
    <td align="right">4.88</td>
    <td align="right">4.92</td>
    <td align="center">5</td>
    <td align="right">2.3236</td>
    <td align="right">4.80</td>
    <td align="right">4.76</td>
    <td align="right">4.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4407</td>
    <td align="right">3.35</td>
    <td align="right">2.99</td>
    <td align="right">3.09</td>
    <td align="center">8</td>
    <td align="right">0.4233</td>
    <td align="right">3.69</td>
    <td align="right">4.72</td>
    <td align="right">4.58</td>
    <td align="center">8</td>
    <td align="right">0.3785</td>
    <td align="right">5.10</td>
    <td align="right">5.32</td>
    <td align="right">4.88</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0864</td>
    <td align="right">9.72</td>
    <td align="right">10.27</td>
    <td align="right">6.01</td>
    <td align="center">11</td>
    <td align="right">0.0777</td>
    <td align="right">9.82</td>
    <td align="right">13.29</td>
    <td align="right">9.39</td>
    <td align="center">11</td>
    <td align="right">0.0640</td>
    <td align="right">11.21</td>
    <td align="right">13.03</td>
    <td align="right">6.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">12.05</td>
    <td align="right">15.54</td>
    <td align="right">9.38</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">14.78</td>
    <td align="right">22.43</td>
    <td align="right">15.09</td>
    <td align="center">14</td>
    <td align="right">0.0114</td>
    <td align="right">17.41</td>
    <td align="right">23.36</td>
    <td align="right">12.63</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.59</td>
    <td align="right">4.15</td>
    <td align="right">3.36</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">9.00</td>
    <td align="right">8.83</td>
    <td align="right">15.36</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.34</td>
    <td align="right">3.99</td>
    <td align="right">4.01</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.93</td>
    <td align="right">4.62</td>
    <td align="right">4.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.29</td>
    <td align="right">14.41</td>
    <td align="right">16.86</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">5.54</td>
    <td align="right">4.58</td>
    <td align="right">4.57</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.51</td>
    <td align="right">5.34</td>
    <td align="right">5.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.46</td>
    <td align="right">16.84</td>
    <td align="right">15.64</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.38</td>
    <td align="right">5.09</td>
    <td align="right">5.15</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.94</td>
    <td align="right">6.00</td>
    <td align="right">5.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">22.27</td>
    <td align="right">21.11</td>
    <td align="right">16.37</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.91</td>
    <td align="right">5.94</td>
    <td align="right">5.73</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.90</td>
    <td align="right">3.34</td>
    <td align="right">3.35</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">3.07</td>
    <td align="right">3.64</td>
    <td align="right">3.59</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.18</td>
    <td align="right">3.54</td>
    <td align="right">3.52</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.60</td>
    <td align="right">2.52</td>
    <td align="right">2.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.74</td>
    <td align="right">3.39</td>
    <td align="right">3.39</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.78</td>
    <td align="right">3.83</td>
    <td align="right">3.76</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.15</td>
    <td align="right">2.28</td>
    <td align="right">2.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.66</td>
    <td align="right">6.25</td>
    <td align="right">6.29</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.84</td>
    <td align="right">6.15</td>
    <td align="right">6.11</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.15</td>
    <td align="right">4.36</td>
    <td align="right">3.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.02</td>
    <td align="right">6.76</td>
    <td align="right">6.57</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.29</td>
    <td align="right">6.94</td>
    <td align="right">7.17</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.22</td>
    <td align="right">4.38</td>
    <td align="right">3.17</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.61</td>
    <td align="right">2.33</td>
    <td align="right">2.34</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.59</td>
    <td align="right">4.04</td>
    <td align="right">4.05</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.76</td>
    <td align="right">3.90</td>
    <td align="right">3.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.75</td>
    <td align="right">2.41</td>
    <td align="right">2.41</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.08</td>
    <td align="right">3.95</td>
    <td align="right">4.27</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">3.88</td>
    <td align="right">4.11</td>
    <td align="right">4.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.37</td>
    <td align="right">4.31</td>
    <td align="right">2.95</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">5.84</td>
    <td align="right">6.16</td>
    <td align="right">4.83</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">5.76</td>
    <td align="right">5.98</td>
    <td align="right">4.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.30</td>
    <td align="right">4.36</td>
    <td align="right">2.98</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">6.88</td>
    <td align="right">7.25</td>
    <td align="right">5.15</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">7.05</td>
    <td align="right">7.22</td>
    <td align="right">4.79</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1818</td>
    <td align="right">10.36</td>
    <td align="right">10.02</td>
    <td align="right">16.42</td>
    <td align="center">4</td>
    <td align="right">3.3670</td>
    <td align="right">4.24</td>
    <td align="right">4.15</td>
    <td align="right">4.14</td>
    <td align="center">5</td>
    <td align="right">3.0480</td>
    <td align="right">4.04</td>
    <td align="right">4.80</td>
    <td align="right">4.77</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3131</td>
    <td align="right">15.75</td>
    <td align="right">15.31</td>
    <td align="right">17.87</td>
    <td align="center">5</td>
    <td align="right">1.0454</td>
    <td align="right">4.68</td>
    <td align="right">4.73</td>
    <td align="right">4.76</td>
    <td align="center">6</td>
    <td align="right">0.8156</td>
    <td align="right">4.72</td>
    <td align="right">5.53</td>
    <td align="right">5.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0462</td>
    <td align="right">18.76</td>
    <td align="right">18.16</td>
    <td align="right">16.77</td>
    <td align="center">6</td>
    <td align="right">0.4073</td>
    <td align="right">5.15</td>
    <td align="right">5.25</td>
    <td align="right">5.46</td>
    <td align="center">7</td>
    <td align="right">0.2848</td>
    <td align="right">5.20</td>
    <td align="right">6.13</td>
    <td align="right">6.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">24.24</td>
    <td align="right">23.32</td>
    <td align="right">17.27</td>
    <td align="center">7</td>
    <td align="right">0.1956</td>
    <td align="right">5.68</td>
    <td align="right">5.96</td>
    <td align="right">5.95</td>
    <td align="center">8</td>
    <td align="right">0.1228</td>
    <td align="right">3.21</td>
    <td align="right">3.52</td>
    <td align="right">3.65</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.22</td>
    <td align="right">3.83</td>
    <td align="right">3.86</td>
    <td align="center">5</td>
    <td align="right">2.3163</td>
    <td align="right">3.38</td>
    <td align="right">3.72</td>
    <td align="right">3.72</td>
    <td align="center">5</td>
    <td align="right">2.7392</td>
    <td align="right">2.85</td>
    <td align="right">2.81</td>
    <td align="right">2.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4226</td>
    <td align="right">3.42</td>
    <td align="right">3.72</td>
    <td align="right">3.69</td>
    <td align="center">8</td>
    <td align="right">0.3730</td>
    <td align="right">3.87</td>
    <td align="right">4.02</td>
    <td align="right">4.11</td>
    <td align="center">8</td>
    <td align="right">0.5386</td>
    <td align="right">2.80</td>
    <td align="right">2.61</td>
    <td align="right">2.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0752</td>
    <td align="right">5.95</td>
    <td align="right">6.62</td>
    <td align="right">6.58</td>
    <td align="center">11</td>
    <td align="right">0.0634</td>
    <td align="right">5.97</td>
    <td align="right">6.54</td>
    <td align="right">6.56</td>
    <td align="center">11</td>
    <td align="right">0.1201</td>
    <td align="right">4.53</td>
    <td align="right">4.78</td>
    <td align="right">3.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0135</td>
    <td align="right">6.31</td>
    <td align="right">7.14</td>
    <td align="right">6.88</td>
    <td align="center">14</td>
    <td align="right">0.0146</td>
    <td align="right">6.82</td>
    <td align="right">7.26</td>
    <td align="right">7.48</td>
    <td align="center">13</td>
    <td align="right">0.0319</td>
    <td align="right">4.64</td>
    <td align="right">4.89</td>
    <td align="right">3.50</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4739</td>
    <td align="right">2.87</td>
    <td align="right">2.73</td>
    <td align="right">2.74</td>
    <td align="center">5</td>
    <td align="right">2.4715</td>
    <td align="right">3.94</td>
    <td align="right">4.44</td>
    <td align="right">4.46</td>
    <td align="center">5</td>
    <td align="right">2.3106</td>
    <td align="right">4.04</td>
    <td align="right">4.42</td>
    <td align="right">4.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4474</td>
    <td align="right">3.02</td>
    <td align="right">2.82</td>
    <td align="right">2.81</td>
    <td align="center">8</td>
    <td align="right">0.4256</td>
    <td align="right">3.75</td>
    <td align="right">4.13</td>
    <td align="right">4.11</td>
    <td align="center">8</td>
    <td align="right">0.3856</td>
    <td align="right">4.22</td>
    <td align="right">4.45</td>
    <td align="right">4.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0914</td>
    <td align="right">4.61</td>
    <td align="right">4.73</td>
    <td align="right">3.31</td>
    <td align="center">11</td>
    <td align="right">0.0757</td>
    <td align="right">6.04</td>
    <td align="right">6.59</td>
    <td align="right">5.22</td>
    <td align="center">11</td>
    <td align="right">0.0638</td>
    <td align="right">6.07</td>
    <td align="right">6.42</td>
    <td align="right">4.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0191</td>
    <td align="right">4.57</td>
    <td align="right">4.71</td>
    <td align="right">3.30</td>
    <td align="center">13</td>
    <td align="right">0.0145</td>
    <td align="right">7.17</td>
    <td align="right">7.59</td>
    <td align="right">5.57</td>
    <td align="center">14</td>
    <td align="right">0.0125</td>
    <td align="right">7.12</td>
    <td align="right">7.47</td>
    <td align="right">5.33</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">38.58</td>
    <td align="right">18.99</td>
    <td align="right">11.52</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">12.10</td>
    <td align="right">12.05</td>
    <td align="right">17.57</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.81</td>
    <td align="right">5.57</td>
    <td align="right">6.06</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.70</td>
    <td align="right">6.73</td>
    <td align="right">6.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">27.61</td>
    <td align="right">28.38</td>
    <td align="right">22.57</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">12.92</td>
    <td align="right">11.19</td>
    <td align="right">11.08</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">10.70</td>
    <td align="right">13.30</td>
    <td align="right">12.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">52.62</td>
    <td align="right">53.82</td>
    <td align="right">23.87</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">14.80</td>
    <td align="right">16.70</td>
    <td align="right">17.49</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">6.73</td>
    <td align="right">8.33</td>
    <td align="right">8.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">33.54</td>
    <td align="right">27.72</td>
    <td align="right">17.00</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">9.60</td>
    <td align="right">12.41</td>
    <td align="right">14.25</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">4.80</td>
    <td align="right">7.62</td>
    <td align="right">6.23</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.63</td>
    <td align="right">4.25</td>
    <td align="right">4.23</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.72</td>
    <td align="right">4.18</td>
    <td align="right">4.22</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.06</td>
    <td align="right">3.05</td>
    <td align="right">3.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.11</td>
    <td align="right">4.04</td>
    <td align="right">3.79</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.13</td>
    <td align="right">4.32</td>
    <td align="right">4.47</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.47</td>
    <td align="right">2.61</td>
    <td align="right">2.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">7.84</td>
    <td align="right">9.79</td>
    <td align="right">8.89</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">7.64</td>
    <td align="right">8.30</td>
    <td align="right">8.52</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">5.59</td>
    <td align="right">6.27</td>
    <td align="right">4.62</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">10.10</td>
    <td align="right">10.77</td>
    <td align="right">11.35</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">9.89</td>
    <td align="right">11.08</td>
    <td align="right">12.57</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">9.74</td>
    <td align="right">9.57</td>
    <td align="right">6.37</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.09</td>
    <td align="right">2.92</td>
    <td align="right">2.99</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.29</td>
    <td align="right">4.81</td>
    <td align="right">4.87</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.45</td>
    <td align="right">4.65</td>
    <td align="right">4.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.09</td>
    <td align="right">2.89</td>
    <td align="right">2.91</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.49</td>
    <td align="right">4.21</td>
    <td align="right">4.23</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">4.26</td>
    <td align="right">4.58</td>
    <td align="right">4.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">6.21</td>
    <td align="right">6.27</td>
    <td align="right">4.96</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">8.37</td>
    <td align="right">8.81</td>
    <td align="right">7.22</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">7.52</td>
    <td align="right">7.75</td>
    <td align="right">6.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">10.15</td>
    <td align="right">11.50</td>
    <td align="right">7.31</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">16.44</td>
    <td align="right">18.27</td>
    <td align="right">9.02</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">13.12</td>
    <td align="right">15.32</td>
    <td align="right">9.39</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1556</td>
    <td align="right">12.26</td>
    <td align="right">12.08</td>
    <td align="right">17.54</td>
    <td align="center">4</td>
    <td align="right">3.3474</td>
    <td align="right">4.95</td>
    <td align="right">4.77</td>
    <td align="right">4.72</td>
    <td align="center">5</td>
    <td align="right">3.0451</td>
    <td align="right">4.86</td>
    <td align="right">5.59</td>
    <td align="right">5.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3152</td>
    <td align="right">19.80</td>
    <td align="right">19.63</td>
    <td align="right">18.92</td>
    <td align="center">5</td>
    <td align="right">1.0335</td>
    <td align="right">6.35</td>
    <td align="right">6.09</td>
    <td align="right">6.23</td>
    <td align="center">6</td>
    <td align="right">0.8296</td>
    <td align="right">5.43</td>
    <td align="right">6.25</td>
    <td align="right">6.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0452</td>
    <td align="right">43.98</td>
    <td align="right">33.37</td>
    <td align="right">20.06</td>
    <td align="center">6</td>
    <td align="right">0.4069</td>
    <td align="right">9.67</td>
    <td align="right">9.53</td>
    <td align="right">9.92</td>
    <td align="center">7</td>
    <td align="right">0.2911</td>
    <td align="right">9.82</td>
    <td align="right">11.44</td>
    <td align="right">10.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">62.29</td>
    <td align="right">66.33</td>
    <td align="right">23.47</td>
    <td align="center">7</td>
    <td align="right">0.1900</td>
    <td align="right">15.97</td>
    <td align="right">15.75</td>
    <td align="right">15.65</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">9.08</td>
    <td align="right">9.01</td>
    <td align="right">10.40</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4408</td>
    <td align="right">3.82</td>
    <td align="right">4.48</td>
    <td align="right">4.50</td>
    <td align="center">5</td>
    <td align="right">2.3114</td>
    <td align="right">3.94</td>
    <td align="right">4.48</td>
    <td align="right">4.47</td>
    <td align="center">5</td>
    <td align="right">2.7422</td>
    <td align="right">3.37</td>
    <td align="right">3.43</td>
    <td align="right">3.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4214</td>
    <td align="right">4.58</td>
    <td align="right">4.51</td>
    <td align="right">4.57</td>
    <td align="center">8</td>
    <td align="right">0.3763</td>
    <td align="right">4.41</td>
    <td align="right">4.98</td>
    <td align="right">4.89</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">3.38</td>
    <td align="right">3.04</td>
    <td align="right">3.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0760</td>
    <td align="right">8.08</td>
    <td align="right">9.81</td>
    <td align="right">9.21</td>
    <td align="center">11</td>
    <td align="right">0.0633</td>
    <td align="right">7.92</td>
    <td align="right">8.73</td>
    <td align="right">12.42</td>
    <td align="center">11</td>
    <td align="right">0.1206</td>
    <td align="right">8.65</td>
    <td align="right">10.69</td>
    <td align="right">6.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0156</td>
    <td align="right">13.06</td>
    <td align="right">13.56</td>
    <td align="right">13.40</td>
    <td align="center">14</td>
    <td align="right">0.0111</td>
    <td align="right">12.74</td>
    <td align="right">14.75</td>
    <td align="right">15.87</td>
    <td align="center">13</td>
    <td align="right">0.0282</td>
    <td align="right">10.11</td>
    <td align="right">13.13</td>
    <td align="right">8.05</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4684</td>
    <td align="right">3.38</td>
    <td align="right">3.28</td>
    <td align="right">3.30</td>
    <td align="center">5</td>
    <td align="right">2.4638</td>
    <td align="right">4.53</td>
    <td align="right">5.17</td>
    <td align="right">5.12</td>
    <td align="center">5</td>
    <td align="right">2.3236</td>
    <td align="right">4.61</td>
    <td align="right">5.07</td>
    <td align="right">5.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4407</td>
    <td align="right">3.56</td>
    <td align="right">3.31</td>
    <td align="right">3.27</td>
    <td align="center">8</td>
    <td align="right">0.4233</td>
    <td align="right">4.30</td>
    <td align="right">4.63</td>
    <td align="right">4.68</td>
    <td align="center">8</td>
    <td align="right">0.3785</td>
    <td align="right">5.13</td>
    <td align="right">5.76</td>
    <td align="right">6.21</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0864</td>
    <td align="right">5.92</td>
    <td align="right">7.54</td>
    <td align="right">6.87</td>
    <td align="center">11</td>
    <td align="right">0.0777</td>
    <td align="right">7.60</td>
    <td align="right">8.67</td>
    <td align="right">7.68</td>
    <td align="center">11</td>
    <td align="right">0.0640</td>
    <td align="right">7.45</td>
    <td align="right">8.51</td>
    <td align="right">6.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">10.70</td>
    <td align="right">12.82</td>
    <td align="right">7.83</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">11.45</td>
    <td align="right">11.65</td>
    <td align="right">8.38</td>
    <td align="center">14</td>
    <td align="right">0.0114</td>
    <td align="right">10.69</td>
    <td align="right">13.03</td>
    <td align="right">7.96</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.29</td>
    <td align="right">6.79</td>
    <td align="right">3.81</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">7.84</td>
    <td align="right">5.01</td>
    <td align="right">14.40</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.81</td>
    <td align="right">1.41</td>
    <td align="right">1.37</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.79</td>
    <td align="right">1.59</td>
    <td align="right">1.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">12.10</td>
    <td align="right">8.02</td>
    <td align="right">13.58</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.92</td>
    <td align="right">1.55</td>
    <td align="right">1.61</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.93</td>
    <td align="right">1.79</td>
    <td align="right">1.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">14.70</td>
    <td align="right">9.82</td>
    <td align="right">12.35</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.76</td>
    <td align="right">1.77</td>
    <td align="right">1.70</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">2.15</td>
    <td align="right">2.30</td>
    <td align="right">1.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">21.60</td>
    <td align="right">12.77</td>
    <td align="right">12.53</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">3.11</td>
    <td align="right">2.18</td>
    <td align="right">1.93</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">1.91</td>
    <td align="right">1.71</td>
    <td align="right">1.70</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">3.54</td>
    <td align="right">2.07</td>
    <td align="right">1.89</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.56</td>
    <td align="right">1.88</td>
    <td align="right">1.87</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.12</td>
    <td align="right">4.13</td>
    <td align="right">2.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.81</td>
    <td align="right">2.24</td>
    <td align="right">2.13</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">2.98</td>
    <td align="right">3.42</td>
    <td align="right">2.71</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.69</td>
    <td align="right">1.51</td>
    <td align="right">1.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">6.87</td>
    <td align="right">3.65</td>
    <td align="right">3.78</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.62</td>
    <td align="right">3.49</td>
    <td align="right">3.47</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.56</td>
    <td align="right">6.26</td>
    <td align="right">3.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.66</td>
    <td align="right">7.47</td>
    <td align="right">6.91</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.37</td>
    <td align="right">4.33</td>
    <td align="right">6.66</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">3.41</td>
    <td align="right">3.47</td>
    <td align="right">1.94</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.25</td>
    <td align="right">2.44</td>
    <td align="right">2.66</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.69</td>
    <td align="right">2.26</td>
    <td align="right">2.15</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.55</td>
    <td align="right">1.96</td>
    <td align="right">2.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.25</td>
    <td align="right">2.60</td>
    <td align="right">2.13</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.07</td>
    <td align="right">3.03</td>
    <td align="right">3.26</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.76</td>
    <td align="right">3.65</td>
    <td align="right">3.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">3.82</td>
    <td align="right">3.44</td>
    <td align="right">2.56</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.26</td>
    <td align="right">5.03</td>
    <td align="right">4.62</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.69</td>
    <td align="right">4.71</td>
    <td align="right">7.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.05</td>
    <td align="right">3.43</td>
    <td align="right">2.16</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">7.44</td>
    <td align="right">5.01</td>
    <td align="right">6.32</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">7.35</td>
    <td align="right">5.13</td>
    <td align="right">5.23</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1818</td>
    <td align="right">8.22</td>
    <td align="right">6.86</td>
    <td align="right">13.97</td>
    <td align="center">4</td>
    <td align="right">3.3670</td>
    <td align="right">1.63</td>
    <td align="right">2.55</td>
    <td align="right">1.94</td>
    <td align="center">5</td>
    <td align="right">3.0480</td>
    <td align="right">2.68</td>
    <td align="right">2.10</td>
    <td align="right">2.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3131</td>
    <td align="right">13.11</td>
    <td align="right">8.93</td>
    <td align="right">16.46</td>
    <td align="center">5</td>
    <td align="right">1.0454</td>
    <td align="right">1.89</td>
    <td align="right">2.74</td>
    <td align="right">2.69</td>
    <td align="center">6</td>
    <td align="right">0.8156</td>
    <td align="right">2.33</td>
    <td align="right">2.63</td>
    <td align="right">2.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0462</td>
    <td align="right">15.22</td>
    <td align="right">10.41</td>
    <td align="right">17.30</td>
    <td align="center">6</td>
    <td align="right">0.4073</td>
    <td align="right">2.30</td>
    <td align="right">2.35</td>
    <td align="right">3.17</td>
    <td align="center">7</td>
    <td align="right">0.2848</td>
    <td align="right">2.68</td>
    <td align="right">2.32</td>
    <td align="right">2.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">20.60</td>
    <td align="right">10.94</td>
    <td align="right">15.11</td>
    <td align="center">7</td>
    <td align="right">0.1956</td>
    <td align="right">2.74</td>
    <td align="right">4.95</td>
    <td align="right">3.41</td>
    <td align="center">8</td>
    <td align="right">0.1228</td>
    <td align="right">3.07</td>
    <td align="right">2.84</td>
    <td align="right">2.65</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.00</td>
    <td align="right">1.88</td>
    <td align="right">2.31</td>
    <td align="center">5</td>
    <td align="right">2.3163</td>
    <td align="right">2.50</td>
    <td align="right">2.84</td>
    <td align="right">2.47</td>
    <td align="center">5</td>
    <td align="right">2.7392</td>
    <td align="right">3.09</td>
    <td align="right">2.02</td>
    <td align="right">1.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4226</td>
    <td align="right">3.16</td>
    <td align="right">2.40</td>
    <td align="right">3.53</td>
    <td align="center">8</td>
    <td align="right">0.3730</td>
    <td align="right">4.08</td>
    <td align="right">3.50</td>
    <td align="right">2.98</td>
    <td align="center">8</td>
    <td align="right">0.5386</td>
    <td align="right">1.95</td>
    <td align="right">2.38</td>
    <td align="right">2.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0752</td>
    <td align="right">5.35</td>
    <td align="right">4.08</td>
    <td align="right">5.09</td>
    <td align="center">11</td>
    <td align="right">0.0634</td>
    <td align="right">7.61</td>
    <td align="right">4.38</td>
    <td align="right">5.21</td>
    <td align="center">11</td>
    <td align="right">0.1201</td>
    <td align="right">3.25</td>
    <td align="right">4.24</td>
    <td align="right">2.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0135</td>
    <td align="right">8.27</td>
    <td align="right">5.88</td>
    <td align="right">5.01</td>
    <td align="center">14</td>
    <td align="right">0.0146</td>
    <td align="right">7.44</td>
    <td align="right">5.58</td>
    <td align="right">6.09</td>
    <td align="center">13</td>
    <td align="right">0.0319</td>
    <td align="right">4.88</td>
    <td align="right">5.46</td>
    <td align="right">2.99</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4739</td>
    <td align="right">3.35</td>
    <td align="right">3.84</td>
    <td align="right">4.24</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.42</td>
    <td align="right">2.59</td>
    <td align="right">2.07</td>
    <td align="center">5</td>
    <td align="right">2.3163</td>
    <td align="right">2.57</td>
    <td align="right">2.37</td>
    <td align="right">2.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4474</td>
    <td align="right">2.67</td>
    <td align="right">3.76</td>
    <td align="right">1.82</td>
    <td align="center">8</td>
    <td align="right">0.4226</td>
    <td align="right">2.75</td>
    <td align="right">2.33</td>
    <td align="right">2.36</td>
    <td align="center">8</td>
    <td align="right">0.3730</td>
    <td align="right">3.26</td>
    <td align="right">3.28</td>
    <td align="right">3.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0914</td>
    <td align="right">3.35</td>
    <td align="right">3.74</td>
    <td align="right">3.04</td>
    <td align="center">11</td>
    <td align="right">0.0752</td>
    <td align="right">5.08</td>
    <td align="right">3.13</td>
    <td align="right">4.37</td>
    <td align="center">11</td>
    <td align="right">0.0634</td>
    <td align="right">4.61</td>
    <td align="right">3.15</td>
    <td align="right">3.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0191</td>
    <td align="right">6.23</td>
    <td align="right">3.72</td>
    <td align="right">2.43</td>
    <td align="center">13</td>
    <td align="right">0.0135</td>
    <td align="right">5.33</td>
    <td align="right">4.26</td>
    <td align="right">5.14</td>
    <td align="center">14</td>
    <td align="right">0.0146</td>
    <td align="right">5.28</td>
    <td align="right">5.58</td>
    <td align="right">5.03</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">30.64</td>
    <td align="right">14.06</td>
    <td align="right">9.01</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">10.45</td>
    <td align="right">13.47</td>
    <td align="right">20.18</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">3.59</td>
    <td align="right">3.35</td>
    <td align="right">4.81</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.24</td>
    <td align="right">4.74</td>
    <td align="right">5.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">38.57</td>
    <td align="right">30.97</td>
    <td align="right">26.67</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">10.94</td>
    <td align="right">9.82</td>
    <td align="right">8.29</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.92</td>
    <td align="right">8.03</td>
    <td align="right">8.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">70.81</td>
    <td align="right">61.71</td>
    <td align="right">35.97</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">16.21</td>
    <td align="right">14.28</td>
    <td align="right">14.29</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">14.99</td>
    <td align="right">14.82</td>
    <td align="right">12.25</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">98.94</td>
    <td align="right">80.60</td>
    <td align="right">45.28</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">22.39</td>
    <td align="right">21.19</td>
    <td align="right">20.59</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">19.84</td>
    <td align="right">16.64</td>
    <td align="right">12.99</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">6.21</td>
    <td align="right">11.95</td>
    <td align="right">21.54</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">8.50</td>
    <td align="right">7.06</td>
    <td align="right">7.64</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">10.26</td>
    <td align="right">12.29</td>
    <td align="right">8.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">9.97</td>
    <td align="right">10.49</td>
    <td align="right">10.97</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">12.53</td>
    <td align="right">24.98</td>
    <td align="right">12.93</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">8.99</td>
    <td align="right">12.52</td>
    <td align="right">12.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">28.64</td>
    <td align="right">19.44</td>
    <td align="right">19.75</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">25.63</td>
    <td align="right">18.91</td>
    <td align="right">20.26</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">15.90</td>
    <td align="right">14.80</td>
    <td align="right">10.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">34.32</td>
    <td align="right">24.66</td>
    <td align="right">24.40</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">29.98</td>
    <td align="right">27.11</td>
    <td align="right">25.33</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">20.75</td>
    <td align="right">19.63</td>
    <td align="right">11.10</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">6.09</td>
    <td align="right">5.41</td>
    <td align="right">4.74</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.82</td>
    <td align="right">8.24</td>
    <td align="right">3.74</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.77</td>
    <td align="right">4.87</td>
    <td align="right">4.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">6.25</td>
    <td align="right">6.61</td>
    <td align="right">6.41</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.60</td>
    <td align="right">10.05</td>
    <td align="right">10.40</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.53</td>
    <td align="right">10.60</td>
    <td align="right">11.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">14.80</td>
    <td align="right">13.94</td>
    <td align="right">10.55</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">22.28</td>
    <td align="right">13.91</td>
    <td align="right">13.22</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">17.19</td>
    <td align="right">12.70</td>
    <td align="right">15.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">13.61</td>
    <td align="right">15.73</td>
    <td align="right">10.52</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">22.28</td>
    <td align="right">21.48</td>
    <td align="right">26.07</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">23.17</td>
    <td align="right">23.02</td>
    <td align="right">22.50</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1556</td>
    <td align="right">11.14</td>
    <td align="right">9.85</td>
    <td align="right">20.95</td>
    <td align="center">4</td>
    <td align="right">3.3474</td>
    <td align="right">3.80</td>
    <td align="right">4.23</td>
    <td align="right">5.08</td>
    <td align="center">5</td>
    <td align="right">3.0451</td>
    <td align="right">3.56</td>
    <td align="right">4.48</td>
    <td align="right">4.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3152</td>
    <td align="right">35.46</td>
    <td align="right">28.07</td>
    <td align="right">25.62</td>
    <td align="center">5</td>
    <td align="right">1.0335</td>
    <td align="right">7.80</td>
    <td align="right">8.49</td>
    <td align="right">8.04</td>
    <td align="center">6</td>
    <td align="right">0.8296</td>
    <td align="right">7.93</td>
    <td align="right">8.74</td>
    <td align="right">5.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0452</td>
    <td align="right">47.81</td>
    <td align="right">38.88</td>
    <td align="right">23.63</td>
    <td align="center">6</td>
    <td align="right">0.4069</td>
    <td align="right">10.45</td>
    <td align="right">10.05</td>
    <td align="right">10.55</td>
    <td align="center">7</td>
    <td align="right">0.2911</td>
    <td align="right">11.98</td>
    <td align="right">10.59</td>
    <td align="right">10.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">76.85</td>
    <td align="right">58.19</td>
    <td align="right">26.88</td>
    <td align="center">7</td>
    <td align="right">0.1900</td>
    <td align="right">10.49</td>
    <td align="right">8.27</td>
    <td align="right">8.83</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">9.50</td>
    <td align="right">8.66</td>
    <td align="right">7.66</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4408</td>
    <td align="right">3.95</td>
    <td align="right">6.33</td>
    <td align="right">4.95</td>
    <td align="center">5</td>
    <td align="right">2.3114</td>
    <td align="right">3.92</td>
    <td align="right">3.76</td>
    <td align="right">3.99</td>
    <td align="center">5</td>
    <td align="right">2.7422</td>
    <td align="right">3.21</td>
    <td align="right">3.25</td>
    <td align="right">4.45</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4214</td>
    <td align="right">5.12</td>
    <td align="right">7.66</td>
    <td align="right">5.01</td>
    <td align="center">8</td>
    <td align="right">0.3763</td>
    <td align="right">4.75</td>
    <td align="right">4.51</td>
    <td align="right">4.55</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">2.70</td>
    <td align="right">3.42</td>
    <td align="right">6.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0760</td>
    <td align="right">14.39</td>
    <td align="right">15.40</td>
    <td align="right">14.92</td>
    <td align="center">11</td>
    <td align="right">0.0633</td>
    <td align="right">16.00</td>
    <td align="right">15.15</td>
    <td align="right">14.93</td>
    <td align="center">11</td>
    <td align="right">0.1206</td>
    <td align="right">13.92</td>
    <td align="right">13.05</td>
    <td align="right">7.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0156</td>
    <td align="right">18.09</td>
    <td align="right">16.97</td>
    <td align="right">17.09</td>
    <td align="center">14</td>
    <td align="right">0.0111</td>
    <td align="right">18.52</td>
    <td align="right">16.45</td>
    <td align="right">15.64</td>
    <td align="center">13</td>
    <td align="right">0.0282</td>
    <td align="right">13.12</td>
    <td align="right">13.31</td>
    <td align="right">7.13</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4684</td>
    <td align="right">2.57</td>
    <td align="right">3.40</td>
    <td align="right">2.98</td>
    <td align="center">5</td>
    <td align="right">2.4408</td>
    <td align="right">3.02</td>
    <td align="right">2.84</td>
    <td align="right">2.87</td>
    <td align="center">5</td>
    <td align="right">2.3114</td>
    <td align="right">2.92</td>
    <td align="right">2.96</td>
    <td align="right">3.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4407</td>
    <td align="right">3.19</td>
    <td align="right">3.66</td>
    <td align="right">3.05</td>
    <td align="center">8</td>
    <td align="right">0.4214</td>
    <td align="right">5.30</td>
    <td align="right">4.95</td>
    <td align="right">5.67</td>
    <td align="center">8</td>
    <td align="right">0.3763</td>
    <td align="right">6.86</td>
    <td align="right">5.42</td>
    <td align="right">8.70</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0864</td>
    <td align="right">9.15</td>
    <td align="right">9.54</td>
    <td align="right">5.60</td>
    <td align="center">11</td>
    <td align="right">0.0760</td>
    <td align="right">11.58</td>
    <td align="right">13.43</td>
    <td align="right">10.66</td>
    <td align="center">11</td>
    <td align="right">0.0633</td>
    <td align="right">16.23</td>
    <td align="right">14.70</td>
    <td align="right">15.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">14.21</td>
    <td align="right">16.51</td>
    <td align="right">10.14</td>
    <td align="center">13</td>
    <td align="right">0.0156</td>
    <td align="right">21.01</td>
    <td align="right">17.47</td>
    <td align="right">16.19</td>
    <td align="center">14</td>
    <td align="right">0.0111</td>
    <td align="right">17.73</td>
    <td align="right">16.72</td>
    <td align="right">14.81</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">34.48</td>
    <td align="right">5.61</td>
    <td align="right">3.80</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">11.93</td>
    <td align="right">12.44</td>
    <td align="right">16.84</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.85</td>
    <td align="right">4.25</td>
    <td align="right">4.26</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.93</td>
    <td align="right">5.27</td>
    <td align="right">5.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.47</td>
    <td align="right">17.68</td>
    <td align="right">17.54</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.90</td>
    <td align="right">4.71</td>
    <td align="right">4.71</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.02</td>
    <td align="right">5.95</td>
    <td align="right">5.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.43</td>
    <td align="right">21.29</td>
    <td align="right">16.55</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.56</td>
    <td align="right">5.27</td>
    <td align="right">5.30</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.36</td>
    <td align="right">6.55</td>
    <td align="right">6.50</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">31.88</td>
    <td align="right">27.34</td>
    <td align="right">17.12</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.90</td>
    <td align="right">6.09</td>
    <td align="right">5.93</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.36</td>
    <td align="right">7.43</td>
    <td align="right">7.56</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">7.84</td>
    <td align="right">5.63</td>
    <td align="right">5.57</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">9.13</td>
    <td align="right">5.57</td>
    <td align="right">5.67</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.38</td>
    <td align="right">3.98</td>
    <td align="right">3.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">12.14</td>
    <td align="right">8.50</td>
    <td align="right">8.51</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">16.78</td>
    <td align="right">7.84</td>
    <td align="right">7.82</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.89</td>
    <td align="right">4.86</td>
    <td align="right">4.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.21</td>
    <td align="right">10.97</td>
    <td align="right">10.92</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.04</td>
    <td align="right">10.50</td>
    <td align="right">10.79</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.03</td>
    <td align="right">7.09</td>
    <td align="right">5.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">16.56</td>
    <td align="right">13.98</td>
    <td align="right">13.97</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">19.00</td>
    <td align="right">13.51</td>
    <td align="right">13.48</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.03</td>
    <td align="right">7.06</td>
    <td align="right">5.28</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">3.26</td>
    <td align="right">3.89</td>
    <td align="right">3.89</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.53</td>
    <td align="right">5.46</td>
    <td align="right">5.52</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.62</td>
    <td align="right">5.40</td>
    <td align="right">5.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.30</td>
    <td align="right">5.56</td>
    <td align="right">4.59</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">4.78</td>
    <td align="right">5.80</td>
    <td align="right">5.02</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">6.92</td>
    <td align="right">7.01</td>
    <td align="right">6.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.03</td>
    <td align="right">6.89</td>
    <td align="right">5.05</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">9.76</td>
    <td align="right">9.30</td>
    <td align="right">7.53</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">9.55</td>
    <td align="right">9.33</td>
    <td align="right">7.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.07</td>
    <td align="right">6.86</td>
    <td align="right">5.03</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">10.32</td>
    <td align="right">10.66</td>
    <td align="right">7.64</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">10.09</td>
    <td align="right">10.26</td>
    <td align="right">7.53</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1818</td>
    <td align="right">13.29</td>
    <td align="right">13.93</td>
    <td align="right">17.85</td>
    <td align="center">4</td>
    <td align="right">3.3670</td>
    <td align="right">6.04</td>
    <td align="right">4.35</td>
    <td align="right">4.39</td>
    <td align="center">5</td>
    <td align="right">3.0480</td>
    <td align="right">7.15</td>
    <td align="right">5.62</td>
    <td align="right">5.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3131</td>
    <td align="right">20.47</td>
    <td align="right">19.45</td>
    <td align="right">18.43</td>
    <td align="center">5</td>
    <td align="right">1.0454</td>
    <td align="right">7.21</td>
    <td align="right">4.85</td>
    <td align="right">5.09</td>
    <td align="center">6</td>
    <td align="right">0.8156</td>
    <td align="right">8.35</td>
    <td align="right">6.10</td>
    <td align="right">6.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0462</td>
    <td align="right">26.52</td>
    <td align="right">23.90</td>
    <td align="right">17.57</td>
    <td align="center">6</td>
    <td align="right">0.4073</td>
    <td align="right">8.91</td>
    <td align="right">5.50</td>
    <td align="right">5.45</td>
    <td align="center">7</td>
    <td align="right">0.2848</td>
    <td align="right">9.69</td>
    <td align="right">6.85</td>
    <td align="right">6.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">34.94</td>
    <td align="right">30.71</td>
    <td align="right">18.08</td>
    <td align="center">7</td>
    <td align="right">0.1956</td>
    <td align="right">10.07</td>
    <td align="right">6.06</td>
    <td align="right">6.11</td>
    <td align="center">8</td>
    <td align="right">0.1228</td>
    <td align="right">10.91</td>
    <td align="right">7.52</td>
    <td align="right">7.55</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">7.96</td>
    <td align="right">5.81</td>
    <td align="right">5.72</td>
    <td align="center">5</td>
    <td align="right">2.3163</td>
    <td align="right">9.18</td>
    <td align="right">5.66</td>
    <td align="right">5.46</td>
    <td align="center">5</td>
    <td align="right">2.7392</td>
    <td align="right">3.42</td>
    <td align="right">3.98</td>
    <td align="right">3.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4226</td>
    <td align="right">12.24</td>
    <td align="right">8.66</td>
    <td align="right">8.60</td>
    <td align="center">8</td>
    <td align="right">0.3730</td>
    <td align="right">20.07</td>
    <td align="right">8.78</td>
    <td align="right">7.86</td>
    <td align="center">8</td>
    <td align="right">0.5386</td>
    <td align="right">2.95</td>
    <td align="right">4.84</td>
    <td align="right">3.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0752</td>
    <td align="right">15.73</td>
    <td align="right">11.40</td>
    <td align="right">11.20</td>
    <td align="center">11</td>
    <td align="right">0.0634</td>
    <td align="right">16.38</td>
    <td align="right">10.78</td>
    <td align="right">10.69</td>
    <td align="center">11</td>
    <td align="right">0.1201</td>
    <td align="right">5.39</td>
    <td align="right">7.03</td>
    <td align="right">5.40</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0135</td>
    <td align="right">17.17</td>
    <td align="right">14.33</td>
    <td align="right">14.34</td>
    <td align="center">14</td>
    <td align="right">0.0146</td>
    <td align="right">19.28</td>
    <td align="right">13.68</td>
    <td align="right">13.77</td>
    <td align="center">13</td>
    <td align="right">0.0319</td>
    <td align="right">5.25</td>
    <td align="right">7.25</td>
    <td align="right">5.37</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4739</td>
    <td align="right">3.29</td>
    <td align="right">3.92</td>
    <td align="right">3.87</td>
    <td align="center">5</td>
    <td align="right">2.4715</td>
    <td align="right">4.53</td>
    <td align="right">5.52</td>
    <td align="right">5.53</td>
    <td align="center">5</td>
    <td align="right">2.3106</td>
    <td align="right">4.64</td>
    <td align="right">5.37</td>
    <td align="right">5.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4474</td>
    <td align="right">3.32</td>
    <td align="right">5.52</td>
    <td align="right">4.61</td>
    <td align="center">8</td>
    <td align="right">0.4256</td>
    <td align="right">4.84</td>
    <td align="right">5.96</td>
    <td align="right">5.13</td>
    <td align="center">8</td>
    <td align="right">0.3856</td>
    <td align="right">6.99</td>
    <td align="right">7.20</td>
    <td align="right">6.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0914</td>
    <td align="right">5.06</td>
    <td align="right">6.90</td>
    <td align="right">5.10</td>
    <td align="center">11</td>
    <td align="right">0.0757</td>
    <td align="right">9.66</td>
    <td align="right">9.66</td>
    <td align="right">7.59</td>
    <td align="center">11</td>
    <td align="right">0.0638</td>
    <td align="right">9.68</td>
    <td align="right">9.22</td>
    <td align="right">7.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0191</td>
    <td align="right">5.29</td>
    <td align="right">7.05</td>
    <td align="right">5.19</td>
    <td align="center">13</td>
    <td align="right">0.0145</td>
    <td align="right">10.15</td>
    <td align="right">11.02</td>
    <td align="right">7.78</td>
    <td align="center">14</td>
    <td align="right">0.0125</td>
    <td align="right">10.37</td>
    <td align="right">10.38</td>
    <td align="right">7.62</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">41.95</td>
    <td align="right">21.33</td>
    <td align="right">8.13</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">14.48</td>
    <td align="right">13.05</td>
    <td align="right">17.72</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">6.96</td>
    <td align="right">4.49</td>
    <td align="right">4.54</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.87</td>
    <td align="right">5.57</td>
    <td align="right">5.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">22.48</td>
    <td align="right">18.93</td>
    <td align="right">18.44</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">8.56</td>
    <td align="right">5.28</td>
    <td align="right">5.16</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.40</td>
    <td align="right">6.41</td>
    <td align="right">6.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">29.77</td>
    <td align="right">26.03</td>
    <td align="right">17.64</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">10.68</td>
    <td align="right">6.26</td>
    <td align="right">6.06</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">11.59</td>
    <td align="right">8.16</td>
    <td align="right">8.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">47.23</td>
    <td align="right">42.40</td>
    <td align="right">20.17</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">15.13</td>
    <td align="right">10.68</td>
    <td align="right">14.28</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">16.74</td>
    <td align="right">13.72</td>
    <td align="right">13.97</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">9.31</td>
    <td align="right">6.32</td>
    <td align="right">6.29</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">9.49</td>
    <td align="right">6.27</td>
    <td align="right">6.31</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.76</td>
    <td align="right">4.25</td>
    <td align="right">4.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">14.79</td>
    <td align="right">10.20</td>
    <td align="right">10.20</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">16.17</td>
    <td align="right">8.70</td>
    <td align="right">8.80</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.34</td>
    <td align="right">5.22</td>
    <td align="right">4.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">18.56</td>
    <td align="right">14.67</td>
    <td align="right">15.01</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">18.95</td>
    <td align="right">12.12</td>
    <td align="right">11.87</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">6.20</td>
    <td align="right">8.56</td>
    <td align="right">6.42</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">23.44</td>
    <td align="right">20.92</td>
    <td align="right">21.07</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">26.70</td>
    <td align="right">19.05</td>
    <td align="right">20.18</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">9.79</td>
    <td align="right">11.30</td>
    <td align="right">8.30</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.66</td>
    <td align="right">4.16</td>
    <td align="right">4.18</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.03</td>
    <td align="right">5.95</td>
    <td align="right">5.91</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.07</td>
    <td align="right">5.85</td>
    <td align="right">5.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.74</td>
    <td align="right">6.04</td>
    <td align="right">4.97</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">5.53</td>
    <td align="right">6.34</td>
    <td align="right">5.67</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">7.93</td>
    <td align="right">7.64</td>
    <td align="right">6.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">6.38</td>
    <td align="right">10.25</td>
    <td align="right">6.13</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">10.92</td>
    <td align="right">10.43</td>
    <td align="right">8.47</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">10.84</td>
    <td align="right">10.35</td>
    <td align="right">8.31</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">9.14</td>
    <td align="right">11.34</td>
    <td align="right">14.68</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">15.02</td>
    <td align="right">14.23</td>
    <td align="right">10.16</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">12.97</td>
    <td align="right">13.94</td>
    <td align="right">9.85</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1556</td>
    <td align="right">15.61</td>
    <td align="right">14.43</td>
    <td align="right">18.75</td>
    <td align="center">4</td>
    <td align="right">3.3474</td>
    <td align="right">7.36</td>
    <td align="right">4.70</td>
    <td align="right">4.68</td>
    <td align="center">5</td>
    <td align="right">3.0451</td>
    <td align="right">8.51</td>
    <td align="right">5.99</td>
    <td align="right">5.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3152</td>
    <td align="right">25.50</td>
    <td align="right">22.71</td>
    <td align="right">19.66</td>
    <td align="center">5</td>
    <td align="right">1.0335</td>
    <td align="right">9.76</td>
    <td align="right">5.79</td>
    <td align="right">6.42</td>
    <td align="center">6</td>
    <td align="right">0.8296</td>
    <td align="right">12.43</td>
    <td align="right">7.88</td>
    <td align="right">7.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0452</td>
    <td align="right">45.85</td>
    <td align="right">35.11</td>
    <td align="right">20.05</td>
    <td align="center">6</td>
    <td align="right">0.4069</td>
    <td align="right">12.81</td>
    <td align="right">8.38</td>
    <td align="right">8.24</td>
    <td align="center">7</td>
    <td align="right">0.2911</td>
    <td align="right">16.60</td>
    <td align="right">11.33</td>
    <td align="right">13.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">76.16</td>
    <td align="right">84.08</td>
    <td align="right">28.24</td>
    <td align="center">7</td>
    <td align="right">0.1900</td>
    <td align="right">23.79</td>
    <td align="right">17.13</td>
    <td align="right">16.52</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">24.22</td>
    <td align="right">19.32</td>
    <td align="right">18.71</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4408</td>
    <td align="right">9.59</td>
    <td align="right">6.48</td>
    <td align="right">6.44</td>
    <td align="center">5</td>
    <td align="right">2.3114</td>
    <td align="right">9.68</td>
    <td align="right">6.04</td>
    <td align="right">5.85</td>
    <td align="center">5</td>
    <td align="right">2.7422</td>
    <td align="right">3.88</td>
    <td align="right">4.25</td>
    <td align="right">4.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4214</td>
    <td align="right">15.04</td>
    <td align="right">10.75</td>
    <td align="right">10.77</td>
    <td align="center">8</td>
    <td align="right">0.3763</td>
    <td align="right">19.01</td>
    <td align="right">12.71</td>
    <td align="right">12.18</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">3.98</td>
    <td align="right">6.07</td>
    <td align="right">4.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0760</td>
    <td align="right">24.30</td>
    <td align="right">18.67</td>
    <td align="right">17.71</td>
    <td align="center">11</td>
    <td align="right">0.0633</td>
    <td align="right">23.41</td>
    <td align="right">22.33</td>
    <td align="right">18.59</td>
    <td align="center">11</td>
    <td align="right">0.1206</td>
    <td align="right">7.55</td>
    <td align="right">11.94</td>
    <td align="right">12.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0156</td>
    <td align="right">30.67</td>
    <td align="right">27.06</td>
    <td align="right">22.31</td>
    <td align="center">14</td>
    <td align="right">0.0111</td>
    <td align="right">28.49</td>
    <td align="right">19.89</td>
    <td align="right">21.23</td>
    <td align="center">13</td>
    <td align="right">0.0282</td>
    <td align="right">13.81</td>
    <td align="right">18.25</td>
    <td align="right">17.15</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4684</td>
    <td align="right">3.66</td>
    <td align="right">4.26</td>
    <td align="right">4.24</td>
    <td align="center">5</td>
    <td align="right">2.4638</td>
    <td align="right">5.20</td>
    <td align="right">5.97</td>
    <td align="right">5.99</td>
    <td align="center">5</td>
    <td align="right">2.3236</td>
    <td align="right">5.11</td>
    <td align="right">5.77</td>
    <td align="right">5.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4407</td>
    <td align="right">3.79</td>
    <td align="right">5.94</td>
    <td align="right">5.02</td>
    <td align="center">8</td>
    <td align="right">0.4233</td>
    <td align="right">5.31</td>
    <td align="right">6.66</td>
    <td align="right">5.58</td>
    <td align="center">8</td>
    <td align="right">0.3785</td>
    <td align="right">7.94</td>
    <td align="right">7.78</td>
    <td align="right">7.20</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0864</td>
    <td align="right">6.65</td>
    <td align="right">10.53</td>
    <td align="right">8.14</td>
    <td align="center">11</td>
    <td align="right">0.0777</td>
    <td align="right">11.52</td>
    <td align="right">11.75</td>
    <td align="right">9.29</td>
    <td align="center">11</td>
    <td align="right">0.0640</td>
    <td align="right">11.89</td>
    <td align="right">11.67</td>
    <td align="right">8.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">12.94</td>
    <td align="right">16.70</td>
    <td align="right">13.46</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">16.22</td>
    <td align="right">19.08</td>
    <td align="right">12.98</td>
    <td align="center">14</td>
    <td align="right">0.0114</td>
    <td align="right">14.89</td>
    <td align="right">18.11</td>
    <td align="right">13.12</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">64.38</td>
    <td align="right">43.90</td>
    <td align="right">19.24</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">27.34</td>
    <td align="right">42.73</td>
    <td align="right">36.69</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.58</td>
    <td align="right">16.06</td>
    <td align="right">16.02</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.20</td>
    <td align="right">19.72</td>
    <td align="right">19.83</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">37.60</td>
    <td align="right">64.30</td>
    <td align="right">39.55</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.33</td>
    <td align="right">19.51</td>
    <td align="right">19.43</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.31</td>
    <td align="right">18.65</td>
    <td align="right">18.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">45.53</td>
    <td align="right">77.92</td>
    <td align="right">38.29</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.18</td>
    <td align="right">18.45</td>
    <td align="right">18.52</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">18.14</td>
    <td align="right">18.55</td>
    <td align="right">18.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">57.44</td>
    <td align="right">97.30</td>
    <td align="right">37.59</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.38</td>
    <td align="right">18.76</td>
    <td align="right">18.81</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">18.90</td>
    <td align="right">20.35</td>
    <td align="right">20.22</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.28</td>
    <td align="right">20.46</td>
    <td align="right">20.57</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.58</td>
    <td align="right">22.22</td>
    <td align="right">22.18</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">10.95</td>
    <td align="right">13.79</td>
    <td align="right">13.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.34</td>
    <td align="right">26.81</td>
    <td align="right">26.76</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.62</td>
    <td align="right">29.22</td>
    <td align="right">28.95</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">12.97</td>
    <td align="right">16.08</td>
    <td align="right">16.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.79</td>
    <td align="right">34.66</td>
    <td align="right">34.17</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">65.32</td>
    <td align="right">47.30</td>
    <td align="right">46.61</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">14.61</td>
    <td align="right">19.62</td>
    <td align="right">19.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">35.04</td>
    <td align="right">37.25</td>
    <td align="right">37.20</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">81.03</td>
    <td align="right">56.65</td>
    <td align="right">56.76</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">24.78</td>
    <td align="right">25.56</td>
    <td align="right">25.53</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">14.76</td>
    <td align="right">16.02</td>
    <td align="right">15.73</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.43</td>
    <td align="right">20.55</td>
    <td align="right">20.46</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">31.28</td>
    <td align="right">22.39</td>
    <td align="right">22.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">19.16</td>
    <td align="right">20.35</td>
    <td align="right">20.45</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.62</td>
    <td align="right">26.95</td>
    <td align="right">26.87</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.91</td>
    <td align="right">29.33</td>
    <td align="right">29.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">28.14</td>
    <td align="right">25.17</td>
    <td align="right">25.19</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.39</td>
    <td align="right">33.68</td>
    <td align="right">33.55</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">65.08</td>
    <td align="right">46.86</td>
    <td align="right">46.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">34.78</td>
    <td align="right">35.45</td>
    <td align="right">35.41</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.74</td>
    <td align="right">36.85</td>
    <td align="right">38.03</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">80.28</td>
    <td align="right">57.88</td>
    <td align="right">57.45</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1768</td>
    <td align="right">28.15</td>
    <td align="right">40.19</td>
    <td align="right">36.99</td>
    <td align="center">4</td>
    <td align="right">3.3657</td>
    <td align="right">12.24</td>
    <td align="right">15.04</td>
    <td align="right">15.00</td>
    <td align="center">5</td>
    <td align="right">3.0599</td>
    <td align="right">13.75</td>
    <td align="right">16.11</td>
    <td align="right">16.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3195</td>
    <td align="right">42.87</td>
    <td align="right">59.28</td>
    <td align="right">38.73</td>
    <td align="center">5</td>
    <td align="right">1.0452</td>
    <td align="right">13.70</td>
    <td align="right">18.41</td>
    <td align="right">17.14</td>
    <td align="center">6</td>
    <td align="right">0.8172</td>
    <td align="right">15.11</td>
    <td align="right">17.07</td>
    <td align="right">17.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0458</td>
    <td align="right">51.98</td>
    <td align="right">73.49</td>
    <td align="right">38.00</td>
    <td align="center">6</td>
    <td align="right">0.4017</td>
    <td align="right">14.72</td>
    <td align="right">17.65</td>
    <td align="right">17.69</td>
    <td align="center">7</td>
    <td align="right">0.2748</td>
    <td align="right">16.60</td>
    <td align="right">17.98</td>
    <td align="right">17.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0055</td>
    <td align="right">65.96</td>
    <td align="right">98.93</td>
    <td align="right">40.82</td>
    <td align="center">7</td>
    <td align="right">0.1892</td>
    <td align="right">16.44</td>
    <td align="right">18.08</td>
    <td align="right">18.19</td>
    <td align="center">8</td>
    <td align="right">0.1217</td>
    <td align="right">15.91</td>
    <td align="right">19.26</td>
    <td align="right">19.67</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4301</td>
    <td align="right">17.29</td>
    <td align="right">20.66</td>
    <td align="right">20.64</td>
    <td align="center">5</td>
    <td align="right">2.3209</td>
    <td align="right">29.52</td>
    <td align="right">20.83</td>
    <td align="right">20.78</td>
    <td align="center">5</td>
    <td align="right">2.7323</td>
    <td align="right">11.43</td>
    <td align="right">13.85</td>
    <td align="right">13.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4075</td>
    <td align="right">21.38</td>
    <td align="right">26.66</td>
    <td align="right">26.73</td>
    <td align="center">8</td>
    <td align="right">0.3787</td>
    <td align="right">40.55</td>
    <td align="right">27.67</td>
    <td align="right">27.80</td>
    <td align="center">8</td>
    <td align="right">0.5321</td>
    <td align="right">13.85</td>
    <td align="right">18.30</td>
    <td align="right">18.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0856</td>
    <td align="right">30.29</td>
    <td align="right">34.41</td>
    <td align="right">34.39</td>
    <td align="center">11</td>
    <td align="right">0.0603</td>
    <td align="right">65.85</td>
    <td align="right">46.30</td>
    <td align="right">46.27</td>
    <td align="center">11</td>
    <td align="right">0.1189</td>
    <td align="right">16.27</td>
    <td align="right">19.86</td>
    <td align="right">19.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0181</td>
    <td align="right">34.78</td>
    <td align="right">36.93</td>
    <td align="right">37.16</td>
    <td align="center">14</td>
    <td align="right">0.0124</td>
    <td align="right">79.87</td>
    <td align="right">56.24</td>
    <td align="right">55.70</td>
    <td align="center">13</td>
    <td align="right">0.0298</td>
    <td align="right">25.31</td>
    <td align="right">25.60</td>
    <td align="right">25.39</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4960</td>
    <td align="right">14.96</td>
    <td align="right">16.08</td>
    <td align="right">16.02</td>
    <td align="center">5</td>
    <td align="right">2.4301</td>
    <td align="right">17.31</td>
    <td align="right">20.70</td>
    <td align="right">20.66</td>
    <td align="center">5</td>
    <td align="right">2.3209</td>
    <td align="right">29.38</td>
    <td align="right">20.83</td>
    <td align="right">20.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4318</td>
    <td align="right">20.45</td>
    <td align="right">20.41</td>
    <td align="right">20.23</td>
    <td align="center">8</td>
    <td align="right">0.4075</td>
    <td align="right">21.54</td>
    <td align="right">26.75</td>
    <td align="right">26.59</td>
    <td align="center">8</td>
    <td align="right">0.3787</td>
    <td align="right">40.52</td>
    <td align="right">27.77</td>
    <td align="right">27.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0968</td>
    <td align="right">28.59</td>
    <td align="right">23.45</td>
    <td align="right">23.43</td>
    <td align="center">11</td>
    <td align="right">0.0856</td>
    <td align="right">30.34</td>
    <td align="right">34.30</td>
    <td align="right">34.84</td>
    <td align="center">11</td>
    <td align="right">0.0603</td>
    <td align="right">65.99</td>
    <td align="right">46.49</td>
    <td align="right">46.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">35.28</td>
    <td align="right">35.57</td>
    <td align="right">36.93</td>
    <td align="center">13</td>
    <td align="right">0.0181</td>
    <td align="right">35.32</td>
    <td align="right">38.82</td>
    <td align="right">36.95</td>
    <td align="center">14</td>
    <td align="right">0.0124</td>
    <td align="right">78.90</td>
    <td align="right">55.38</td>
    <td align="right">55.64</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">90.26</td>
    <td align="right">120.63</td>
    <td align="right">31.51</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">31.78</td>
    <td align="right">62.22</td>
    <td align="right">50.29</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">15.33</td>
    <td align="right">20.94</td>
    <td align="right">26.39</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">35.21</td>
    <td align="right">25.53</td>
    <td align="right">26.23</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">74.21</td>
    <td align="right">173.82</td>
    <td align="right">74.00</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">31.64</td>
    <td align="right">41.47</td>
    <td align="right">46.99</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">35.24</td>
    <td align="right">39.92</td>
    <td align="right">42.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">143.35</td>
    <td align="right">239.99</td>
    <td align="right">94.11</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">50.82</td>
    <td align="right">51.11</td>
    <td align="right">46.91</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">49.51</td>
    <td align="right">48.00</td>
    <td align="right">47.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">212.18</td>
    <td align="right">372.27</td>
    <td align="right">105.96</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">54.76</td>
    <td align="right">53.13</td>
    <td align="right">58.17</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">53.44</td>
    <td align="right">53.81</td>
    <td align="right">55.84</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">22.95</td>
    <td align="right">31.02</td>
    <td align="right">26.44</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">59.87</td>
    <td align="right">29.87</td>
    <td align="right">29.77</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">12.58</td>
    <td align="right">19.75</td>
    <td align="right">16.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">46.16</td>
    <td align="right">51.27</td>
    <td align="right">49.34</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">110.98</td>
    <td align="right">64.50</td>
    <td align="right">60.41</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">30.53</td>
    <td align="right">29.78</td>
    <td align="right">35.72</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">88.43</td>
    <td align="right">112.09</td>
    <td align="right">114.60</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">111.62</td>
    <td align="right">98.93</td>
    <td align="right">104.33</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">48.24</td>
    <td align="right">56.40</td>
    <td align="right">56.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">94.55</td>
    <td align="right">105.75</td>
    <td align="right">107.99</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">142.53</td>
    <td align="right">116.60</td>
    <td align="right">115.12</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">62.86</td>
    <td align="right">64.62</td>
    <td align="right">65.06</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">20.74</td>
    <td align="right">25.03</td>
    <td align="right">19.25</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">35.44</td>
    <td align="right">30.43</td>
    <td align="right">27.95</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">69.69</td>
    <td align="right">29.34</td>
    <td align="right">29.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">43.52</td>
    <td align="right">49.69</td>
    <td align="right">50.31</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">45.19</td>
    <td align="right">52.46</td>
    <td align="right">54.33</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">111.18</td>
    <td align="right">64.68</td>
    <td align="right">62.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">93.35</td>
    <td align="right">61.67</td>
    <td align="right">62.30</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">84.67</td>
    <td align="right">99.51</td>
    <td align="right">99.17</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">110.93</td>
    <td align="right">93.42</td>
    <td align="right">92.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">108.84</td>
    <td align="right">112.46</td>
    <td align="right">112.78</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">93.23</td>
    <td align="right">109.14</td>
    <td align="right">105.37</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">141.78</td>
    <td align="right">119.71</td>
    <td align="right">116.34</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1542</td>
    <td align="right">30.02</td>
    <td align="right">43.91</td>
    <td align="right">44.40</td>
    <td align="center">4</td>
    <td align="right">3.3491</td>
    <td align="right">14.62</td>
    <td align="right">17.90</td>
    <td align="right">19.02</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">17.12</td>
    <td align="right">21.19</td>
    <td align="right">21.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">70.13</td>
    <td align="right">111.34</td>
    <td align="right">67.69</td>
    <td align="center">5</td>
    <td align="right">1.0294</td>
    <td align="right">28.45</td>
    <td align="right">41.14</td>
    <td align="right">40.65</td>
    <td align="center">6</td>
    <td align="right">0.8254</td>
    <td align="right">40.66</td>
    <td align="right">42.61</td>
    <td align="right">45.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0451</td>
    <td align="right">173.85</td>
    <td align="right">174.61</td>
    <td align="right">57.48</td>
    <td align="center">6</td>
    <td align="right">0.4029</td>
    <td align="right">19.87</td>
    <td align="right">22.67</td>
    <td align="right">24.42</td>
    <td align="center">7</td>
    <td align="right">0.2903</td>
    <td align="right">23.34</td>
    <td align="right">28.42</td>
    <td align="right">22.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">141.99</td>
    <td align="right">359.65</td>
    <td align="right">104.19</td>
    <td align="center">7</td>
    <td align="right">0.1877</td>
    <td align="right">44.14</td>
    <td align="right">46.32</td>
    <td align="right">53.75</td>
    <td align="center">8</td>
    <td align="right">0.1191</td>
    <td align="right">55.77</td>
    <td align="right">55.96</td>
    <td align="right">54.51</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">19.04</td>
    <td align="right">22.63</td>
    <td align="right">22.80</td>
    <td align="center">5</td>
    <td align="right">2.3116</td>
    <td align="right">33.73</td>
    <td align="right">23.09</td>
    <td align="right">23.60</td>
    <td align="center">5</td>
    <td align="right">2.7367</td>
    <td align="right">16.26</td>
    <td align="right">15.13</td>
    <td align="right">15.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4206</td>
    <td align="right">31.16</td>
    <td align="right">39.69</td>
    <td align="right">48.08</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">75.03</td>
    <td align="right">49.37</td>
    <td align="right">49.94</td>
    <td align="center">8</td>
    <td align="right">0.5431</td>
    <td align="right">19.51</td>
    <td align="right">31.03</td>
    <td align="right">26.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0786</td>
    <td align="right">83.88</td>
    <td align="right">85.76</td>
    <td align="right">86.18</td>
    <td align="center">11</td>
    <td align="right">0.0636</td>
    <td align="right">82.12</td>
    <td align="right">97.95</td>
    <td align="right">59.84</td>
    <td align="center">11</td>
    <td align="right">0.1181</td>
    <td align="right">23.36</td>
    <td align="right">33.27</td>
    <td align="right">35.40</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">59.61</td>
    <td align="right">84.10</td>
    <td align="right">88.93</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">115.02</td>
    <td align="right">98.46</td>
    <td align="right">82.04</td>
    <td align="center">13</td>
    <td align="right">0.0278</td>
    <td align="right">57.44</td>
    <td align="right">67.04</td>
    <td align="right">67.36</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4684</td>
    <td align="right">16.57</td>
    <td align="right">16.97</td>
    <td align="right">16.98</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">19.15</td>
    <td align="right">22.93</td>
    <td align="right">24.12</td>
    <td align="center">5</td>
    <td align="right">2.3116</td>
    <td align="right">36.39</td>
    <td align="right">28.81</td>
    <td align="right">23.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4426</td>
    <td align="right">25.26</td>
    <td align="right">24.35</td>
    <td align="right">27.64</td>
    <td align="center">8</td>
    <td align="right">0.4206</td>
    <td align="right">27.53</td>
    <td align="right">48.85</td>
    <td align="right">65.43</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">106.37</td>
    <td align="right">51.51</td>
    <td align="right">56.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0868</td>
    <td align="right">101.90</td>
    <td align="right">64.45</td>
    <td align="right">73.31</td>
    <td align="center">11</td>
    <td align="right">0.0786</td>
    <td align="right">99.02</td>
    <td align="right">110.18</td>
    <td align="right">120.81</td>
    <td align="center">11</td>
    <td align="right">0.0636</td>
    <td align="right">115.36</td>
    <td align="right">106.40</td>
    <td align="right">74.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">117.33</td>
    <td align="right">101.26</td>
    <td align="right">92.52</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">68.09</td>
    <td align="right">82.94</td>
    <td align="right">72.51</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">110.34</td>
    <td align="right">88.61</td>
    <td align="right">81.57</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">62.64</td>
    <td align="right">10.36</td>
    <td align="right">6.93</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">13.85</td>
    <td align="right">22.86</td>
    <td align="right">26.67</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">9.54</td>
    <td align="right">12.36</td>
    <td align="right">12.36</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">11.69</td>
    <td align="right">13.85</td>
    <td align="right">13.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">19.55</td>
    <td align="right">34.92</td>
    <td align="right">28.76</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">12.00</td>
    <td align="right">14.05</td>
    <td align="right">14.10</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">13.45</td>
    <td align="right">15.31</td>
    <td align="right">15.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">25.20</td>
    <td align="right">47.53</td>
    <td align="right">29.96</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">13.73</td>
    <td align="right">15.33</td>
    <td align="right">15.32</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">14.62</td>
    <td align="right">16.78</td>
    <td align="right">16.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">32.72</td>
    <td align="right">60.83</td>
    <td align="right">30.80</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">14.68</td>
    <td align="right">16.34</td>
    <td align="right">16.26</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">15.94</td>
    <td align="right">17.81</td>
    <td align="right">17.74</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.68</td>
    <td align="right">16.09</td>
    <td align="right">16.11</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.29</td>
    <td align="right">16.77</td>
    <td align="right">16.74</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">7.02</td>
    <td align="right">9.33</td>
    <td align="right">9.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.39</td>
    <td align="right">22.35</td>
    <td align="right">22.43</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.38</td>
    <td align="right">22.41</td>
    <td align="right">22.38</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">12.32</td>
    <td align="right">13.94</td>
    <td align="right">14.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.10</td>
    <td align="right">31.99</td>
    <td align="right">31.38</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.62</td>
    <td align="right">30.87</td>
    <td align="right">30.80</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.67</td>
    <td align="right">17.53</td>
    <td align="right">17.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">27.06</td>
    <td align="right">35.63</td>
    <td align="right">35.62</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">32.92</td>
    <td align="right">35.90</td>
    <td align="right">35.79</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">16.38</td>
    <td align="right">20.56</td>
    <td align="right">20.58</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">6.56</td>
    <td align="right">9.39</td>
    <td align="right">9.37</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.80</td>
    <td align="right">16.18</td>
    <td align="right">16.15</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.26</td>
    <td align="right">16.78</td>
    <td align="right">16.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">10.77</td>
    <td align="right">13.73</td>
    <td align="right">13.75</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.39</td>
    <td align="right">22.34</td>
    <td align="right">22.45</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.35</td>
    <td align="right">22.51</td>
    <td align="right">22.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">13.10</td>
    <td align="right">17.60</td>
    <td align="right">17.63</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.23</td>
    <td align="right">32.05</td>
    <td align="right">31.31</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.62</td>
    <td align="right">30.77</td>
    <td align="right">30.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">16.01</td>
    <td align="right">20.94</td>
    <td align="right">20.93</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">27.15</td>
    <td align="right">35.60</td>
    <td align="right">35.58</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.27</td>
    <td align="right">35.76</td>
    <td align="right">35.73</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1768</td>
    <td align="right">19.22</td>
    <td align="right">27.88</td>
    <td align="right">28.30</td>
    <td align="center">4</td>
    <td align="right">3.3657</td>
    <td align="right">9.63</td>
    <td align="right">12.43</td>
    <td align="right">12.45</td>
    <td align="center">5</td>
    <td align="right">3.0599</td>
    <td align="right">12.48</td>
    <td align="right">14.61</td>
    <td align="right">14.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3195</td>
    <td align="right">28.42</td>
    <td align="right">42.33</td>
    <td align="right">30.74</td>
    <td align="center">5</td>
    <td align="right">1.0452</td>
    <td align="right">13.06</td>
    <td align="right">14.97</td>
    <td align="right">14.95</td>
    <td align="center">6</td>
    <td align="right">0.8172</td>
    <td align="right">14.47</td>
    <td align="right">15.95</td>
    <td align="right">15.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0458</td>
    <td align="right">34.75</td>
    <td align="right">54.07</td>
    <td align="right">29.84</td>
    <td align="center">6</td>
    <td align="right">0.4017</td>
    <td align="right">14.61</td>
    <td align="right">16.27</td>
    <td align="right">16.48</td>
    <td align="center">7</td>
    <td align="right">0.2748</td>
    <td align="right">15.21</td>
    <td align="right">17.27</td>
    <td align="right">17.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0055</td>
    <td align="right">48.68</td>
    <td align="right">68.45</td>
    <td align="right">30.77</td>
    <td align="center">7</td>
    <td align="right">0.1892</td>
    <td align="right">15.61</td>
    <td align="right">17.42</td>
    <td align="right">17.33</td>
    <td align="center">8</td>
    <td align="right">0.1217</td>
    <td align="right">16.85</td>
    <td align="right">18.86</td>
    <td align="right">18.84</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4301</td>
    <td align="right">13.29</td>
    <td align="right">16.88</td>
    <td align="right">16.83</td>
    <td align="center">5</td>
    <td align="right">2.3209</td>
    <td align="right">14.69</td>
    <td align="right">16.27</td>
    <td align="right">16.30</td>
    <td align="center">5</td>
    <td align="right">2.7323</td>
    <td align="right">7.06</td>
    <td align="right">8.99</td>
    <td align="right">9.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4075</td>
    <td align="right">17.98</td>
    <td align="right">25.50</td>
    <td align="right">25.49</td>
    <td align="center">8</td>
    <td align="right">0.3787</td>
    <td align="right">18.96</td>
    <td align="right">23.72</td>
    <td align="right">23.75</td>
    <td align="center">8</td>
    <td align="right">0.5321</td>
    <td align="right">10.79</td>
    <td align="right">13.35</td>
    <td align="right">13.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0856</td>
    <td align="right">25.04</td>
    <td align="right">32.55</td>
    <td align="right">32.53</td>
    <td align="center">11</td>
    <td align="right">0.0603</td>
    <td align="right">27.69</td>
    <td align="right">31.14</td>
    <td align="right">31.12</td>
    <td align="center">11</td>
    <td align="right">0.1189</td>
    <td align="right">13.20</td>
    <td align="right">17.97</td>
    <td align="right">17.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0181</td>
    <td align="right">28.28</td>
    <td align="right">35.93</td>
    <td align="right">35.96</td>
    <td align="center">14</td>
    <td align="right">0.0124</td>
    <td align="right">33.60</td>
    <td align="right">38.30</td>
    <td align="right">38.23</td>
    <td align="center">13</td>
    <td align="right">0.0298</td>
    <td align="right">17.22</td>
    <td align="right">20.83</td>
    <td align="right">20.75</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4960</td>
    <td align="right">6.72</td>
    <td align="right">9.47</td>
    <td align="right">9.48</td>
    <td align="center">5</td>
    <td align="right">2.4301</td>
    <td align="right">13.97</td>
    <td align="right">16.92</td>
    <td align="right">16.86</td>
    <td align="center">5</td>
    <td align="right">2.3209</td>
    <td align="right">14.72</td>
    <td align="right">16.41</td>
    <td align="right">16.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4318</td>
    <td align="right">10.42</td>
    <td align="right">13.86</td>
    <td align="right">13.86</td>
    <td align="center">8</td>
    <td align="right">0.4075</td>
    <td align="right">18.01</td>
    <td align="right">25.51</td>
    <td align="right">25.49</td>
    <td align="center">8</td>
    <td align="right">0.3787</td>
    <td align="right">18.95</td>
    <td align="right">23.68</td>
    <td align="right">23.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0968</td>
    <td align="right">14.32</td>
    <td align="right">17.50</td>
    <td align="right">17.49</td>
    <td align="center">11</td>
    <td align="right">0.0856</td>
    <td align="right">25.04</td>
    <td align="right">32.61</td>
    <td align="right">32.59</td>
    <td align="center">11</td>
    <td align="right">0.0603</td>
    <td align="right">27.71</td>
    <td align="right">31.10</td>
    <td align="right">31.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">17.88</td>
    <td align="right">20.90</td>
    <td align="right">20.64</td>
    <td align="center">13</td>
    <td align="right">0.0181</td>
    <td align="right">28.41</td>
    <td align="right">36.09</td>
    <td align="right">35.98</td>
    <td align="center">14</td>
    <td align="right">0.0124</td>
    <td align="right">33.64</td>
    <td align="right">38.31</td>
    <td align="right">38.33</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">80.39</td>
    <td align="right">46.99</td>
    <td align="right">10.68</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">14.31</td>
    <td align="right">23.37</td>
    <td align="right">28.60</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">9.87</td>
    <td align="right">12.77</td>
    <td align="right">12.83</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">12.10</td>
    <td align="right">14.26</td>
    <td align="right">14.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">19.49</td>
    <td align="right">35.24</td>
    <td align="right">29.54</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">12.16</td>
    <td align="right">14.10</td>
    <td align="right">14.02</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">14.51</td>
    <td align="right">16.07</td>
    <td align="right">15.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">25.81</td>
    <td align="right">56.74</td>
    <td align="right">36.83</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">14.32</td>
    <td align="right">16.26</td>
    <td align="right">16.27</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">15.31</td>
    <td align="right">17.54</td>
    <td align="right">17.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">40.46</td>
    <td align="right">74.87</td>
    <td align="right">32.89</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">18.95</td>
    <td align="right">19.02</td>
    <td align="right">21.45</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">20.27</td>
    <td align="right">24.04</td>
    <td align="right">22.76</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">12.99</td>
    <td align="right">17.12</td>
    <td align="right">17.18</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.61</td>
    <td align="right">17.93</td>
    <td align="right">17.95</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">7.35</td>
    <td align="right">9.68</td>
    <td align="right">9.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">17.26</td>
    <td align="right">22.37</td>
    <td align="right">22.51</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">18.79</td>
    <td align="right">23.37</td>
    <td align="right">23.30</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">11.81</td>
    <td align="right">14.69</td>
    <td align="right">14.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">27.78</td>
    <td align="right">36.28</td>
    <td align="right">37.49</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">30.42</td>
    <td align="right">39.21</td>
    <td align="right">36.31</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">13.70</td>
    <td align="right">18.49</td>
    <td align="right">18.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">35.96</td>
    <td align="right">44.80</td>
    <td align="right">43.57</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">45.11</td>
    <td align="right">44.13</td>
    <td align="right">41.12</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">30.98</td>
    <td align="right">29.96</td>
    <td align="right">30.64</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">6.86</td>
    <td align="right">9.83</td>
    <td align="right">9.81</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">12.98</td>
    <td align="right">17.15</td>
    <td align="right">17.12</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.66</td>
    <td align="right">17.98</td>
    <td align="right">17.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">12.45</td>
    <td align="right">15.01</td>
    <td align="right">14.42</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">18.76</td>
    <td align="right">24.71</td>
    <td align="right">23.29</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">18.88</td>
    <td align="right">23.54</td>
    <td align="right">24.72</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">13.66</td>
    <td align="right">19.83</td>
    <td align="right">18.36</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">27.74</td>
    <td align="right">36.50</td>
    <td align="right">37.33</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">35.88</td>
    <td align="right">35.07</td>
    <td align="right">35.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">25.85</td>
    <td align="right">31.03</td>
    <td align="right">38.13</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">33.00</td>
    <td align="right">46.41</td>
    <td align="right">52.14</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">39.45</td>
    <td align="right">43.32</td>
    <td align="right">42.65</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1542</td>
    <td align="right">19.95</td>
    <td align="right">28.93</td>
    <td align="right">30.93</td>
    <td align="center">4</td>
    <td align="right">3.3491</td>
    <td align="right">9.91</td>
    <td align="right">12.96</td>
    <td align="right">13.00</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">12.91</td>
    <td align="right">15.02</td>
    <td align="right">15.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">28.79</td>
    <td align="right">43.52</td>
    <td align="right">31.90</td>
    <td align="center">5</td>
    <td align="right">1.0294</td>
    <td align="right">12.92</td>
    <td align="right">14.92</td>
    <td align="right">14.85</td>
    <td align="center">6</td>
    <td align="right">0.8254</td>
    <td align="right">14.65</td>
    <td align="right">16.47</td>
    <td align="right">16.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0451</td>
    <td align="right">39.36</td>
    <td align="right">63.56</td>
    <td align="right">36.02</td>
    <td align="center">6</td>
    <td align="right">0.4029</td>
    <td align="right">16.39</td>
    <td align="right">23.39</td>
    <td align="right">19.95</td>
    <td align="center">7</td>
    <td align="right">0.2903</td>
    <td align="right">16.47</td>
    <td align="right">19.30</td>
    <td align="right">18.24</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">61.44</td>
    <td align="right">87.19</td>
    <td align="right">37.82</td>
    <td align="center">7</td>
    <td align="right">0.1877</td>
    <td align="right">18.23</td>
    <td align="right">28.30</td>
    <td align="right">30.84</td>
    <td align="center">8</td>
    <td align="right">0.1191</td>
    <td align="right">32.82</td>
    <td align="right">32.59</td>
    <td align="right">33.61</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">14.53</td>
    <td align="right">21.67</td>
    <td align="right">17.85</td>
    <td align="center">5</td>
    <td align="right">2.3116</td>
    <td align="right">15.36</td>
    <td align="right">17.07</td>
    <td align="right">17.27</td>
    <td align="center">5</td>
    <td align="right">2.7367</td>
    <td align="right">7.35</td>
    <td align="right">9.32</td>
    <td align="right">9.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4206</td>
    <td align="right">19.14</td>
    <td align="right">27.86</td>
    <td align="right">46.32</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">20.20</td>
    <td align="right">23.83</td>
    <td align="right">25.57</td>
    <td align="center">8</td>
    <td align="right">0.5431</td>
    <td align="right">11.26</td>
    <td align="right">13.58</td>
    <td align="right">13.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0786</td>
    <td align="right">28.17</td>
    <td align="right">38.49</td>
    <td align="right">45.39</td>
    <td align="center">11</td>
    <td align="right">0.0636</td>
    <td align="right">34.85</td>
    <td align="right">40.14</td>
    <td align="right">36.00</td>
    <td align="center">11</td>
    <td align="right">0.1181</td>
    <td align="right">14.54</td>
    <td align="right">19.22</td>
    <td align="right">19.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">36.83</td>
    <td align="right">47.56</td>
    <td align="right">48.61</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">44.22</td>
    <td align="right">47.03</td>
    <td align="right">48.67</td>
    <td align="center">13</td>
    <td align="right">0.0278</td>
    <td align="right">27.88</td>
    <td align="right">31.30</td>
    <td align="right">31.58</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4684</td>
    <td align="right">7.05</td>
    <td align="right">9.96</td>
    <td align="right">10.04</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">13.87</td>
    <td align="right">17.46</td>
    <td align="right">17.86</td>
    <td align="center">5</td>
    <td align="right">2.3116</td>
    <td align="right">15.27</td>
    <td align="right">17.15</td>
    <td align="right">17.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4426</td>
    <td align="right">10.61</td>
    <td align="right">13.98</td>
    <td align="right">13.83</td>
    <td align="center">8</td>
    <td align="right">0.4206</td>
    <td align="right">19.62</td>
    <td align="right">26.02</td>
    <td align="right">25.67</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">19.90</td>
    <td align="right">24.44</td>
    <td align="right">23.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0868</td>
    <td align="right">15.52</td>
    <td align="right">19.66</td>
    <td align="right">18.27</td>
    <td align="center">11</td>
    <td align="right">0.0786</td>
    <td align="right">29.45</td>
    <td align="right">39.81</td>
    <td align="right">38.56</td>
    <td align="center">11</td>
    <td align="right">0.0636</td>
    <td align="right">35.38</td>
    <td align="right">40.86</td>
    <td align="right">36.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">24.59</td>
    <td align="right">28.93</td>
    <td align="right">27.95</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">32.59</td>
    <td align="right">43.30</td>
    <td align="right">43.94</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">39.92</td>
    <td align="right">41.94</td>
    <td align="right">42.24</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">43.10</td>
    <td align="right">8.64</td>
    <td align="right">6.30</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">59.32</td>
    <td align="right">59.69</td>
    <td align="right">44.21</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">21.82</td>
    <td align="right">20.48</td>
    <td align="right">24.54</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">25.13</td>
    <td align="right">26.04</td>
    <td align="right">29.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">89.45</td>
    <td align="right">80.78</td>
    <td align="right">44.12</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">23.84</td>
    <td align="right">22.13</td>
    <td align="right">24.44</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">26.84</td>
    <td align="right">28.52</td>
    <td align="right">30.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">110.42</td>
    <td align="right">102.19</td>
    <td align="right">45.59</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">25.18</td>
    <td align="right">22.80</td>
    <td align="right">24.28</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">29.80</td>
    <td align="right">30.45</td>
    <td align="right">31.64</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">139.97</td>
    <td align="right">123.15</td>
    <td align="right">43.81</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">27.89</td>
    <td align="right">24.37</td>
    <td align="right">25.21</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">31.27</td>
    <td align="right">33.92</td>
    <td align="right">33.88</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">23.51</td>
    <td align="right">44.85</td>
    <td align="right">44.89</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">27.18</td>
    <td align="right">45.31</td>
    <td align="right">45.75</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">18.67</td>
    <td align="right">25.56</td>
    <td align="right">25.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">28.32</td>
    <td align="right">61.04</td>
    <td align="right">61.00</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">33.48</td>
    <td align="right">62.27</td>
    <td align="right">62.83</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">25.54</td>
    <td align="right">36.36</td>
    <td align="right">25.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">40.21</td>
    <td align="right">80.95</td>
    <td align="right">81.45</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">45.15</td>
    <td align="right">83.79</td>
    <td align="right">82.29</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">29.02</td>
    <td align="right">55.03</td>
    <td align="right">39.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">43.89</td>
    <td align="right">92.02</td>
    <td align="right">92.45</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">52.22</td>
    <td align="right">97.78</td>
    <td align="right">97.66</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">29.49</td>
    <td align="right">55.74</td>
    <td align="right">39.97</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4823</td>
    <td align="right">18.65</td>
    <td align="right">26.34</td>
    <td align="right">26.21</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">20.73</td>
    <td align="right">29.43</td>
    <td align="right">29.20</td>
    <td align="center">5</td>
    <td align="right">2.3084</td>
    <td align="right">20.92</td>
    <td align="right">30.90</td>
    <td align="right">31.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4562</td>
    <td align="right">18.99</td>
    <td align="right">46.62</td>
    <td align="right">35.69</td>
    <td align="center">8</td>
    <td align="right">0.4164</td>
    <td align="right">18.68</td>
    <td align="right">40.35</td>
    <td align="right">28.79</td>
    <td align="center">8</td>
    <td align="right">0.3847</td>
    <td align="right">21.01</td>
    <td align="right">52.04</td>
    <td align="right">39.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">28.74</td>
    <td align="right">54.56</td>
    <td align="right">38.91</td>
    <td align="center">11</td>
    <td align="right">0.0758</td>
    <td align="right">32.98</td>
    <td align="right">53.05</td>
    <td align="right">35.35</td>
    <td align="center">11</td>
    <td align="right">0.0626</td>
    <td align="right">32.19</td>
    <td align="right">61.20</td>
    <td align="right">43.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0188</td>
    <td align="right">28.83</td>
    <td align="right">54.76</td>
    <td align="right">39.69</td>
    <td align="center">13</td>
    <td align="right">0.0109</td>
    <td align="right">33.52</td>
    <td align="right">65.01</td>
    <td align="right">44.36</td>
    <td align="center">14</td>
    <td align="right">0.0103</td>
    <td align="right">33.30</td>
    <td align="right">64.15</td>
    <td align="right">44.82</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1768</td>
    <td align="right">91.04</td>
    <td align="right">83.58</td>
    <td align="right">54.53</td>
    <td align="center">4</td>
    <td align="right">3.3657</td>
    <td align="right">27.09</td>
    <td align="right">25.44</td>
    <td align="right">29.64</td>
    <td align="center">5</td>
    <td align="right">3.0599</td>
    <td align="right">30.59</td>
    <td align="right">29.91</td>
    <td align="right">32.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3195</td>
    <td align="right">139.58</td>
    <td align="right">123.59</td>
    <td align="right">56.11</td>
    <td align="center">5</td>
    <td align="right">1.0452</td>
    <td align="right">29.18</td>
    <td align="right">27.26</td>
    <td align="right">29.39</td>
    <td align="center">6</td>
    <td align="right">0.8172</td>
    <td align="right">31.98</td>
    <td align="right">31.46</td>
    <td align="right">33.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0458</td>
    <td align="right">171.58</td>
    <td align="right">148.21</td>
    <td align="right">54.63</td>
    <td align="center">6</td>
    <td align="right">0.4017</td>
    <td align="right">30.32</td>
    <td align="right">27.84</td>
    <td align="right">29.21</td>
    <td align="center">7</td>
    <td align="right">0.2748</td>
    <td align="right">34.73</td>
    <td align="right">34.68</td>
    <td align="right">35.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0055</td>
    <td align="right">219.45</td>
    <td align="right">186.68</td>
    <td align="right">55.06</td>
    <td align="center">7</td>
    <td align="right">0.1892</td>
    <td align="right">32.58</td>
    <td align="right">29.59</td>
    <td align="right">30.24</td>
    <td align="center">8</td>
    <td align="right">0.1217</td>
    <td align="right">36.38</td>
    <td align="right">36.16</td>
    <td align="right">36.60</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4301</td>
    <td align="right">28.58</td>
    <td align="right">46.23</td>
    <td align="right">46.51</td>
    <td align="center">5</td>
    <td align="right">2.3209</td>
    <td align="right">32.46</td>
    <td align="right">47.26</td>
    <td align="right">47.83</td>
    <td align="center">5</td>
    <td align="right">2.7313</td>
    <td align="right">22.45</td>
    <td align="right">26.80</td>
    <td align="right">26.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4075</td>
    <td align="right">32.54</td>
    <td align="right">62.74</td>
    <td align="right">65.70</td>
    <td align="center">8</td>
    <td align="right">0.3787</td>
    <td align="right">77.28</td>
    <td align="right">63.51</td>
    <td align="right">65.08</td>
    <td align="center">8</td>
    <td align="right">0.5366</td>
    <td align="right">22.57</td>
    <td align="right">38.34</td>
    <td align="right">26.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0856</td>
    <td align="right">44.93</td>
    <td align="right">86.12</td>
    <td align="right">86.07</td>
    <td align="center">11</td>
    <td align="right">0.0603</td>
    <td align="right">51.09</td>
    <td align="right">87.35</td>
    <td align="right">86.23</td>
    <td align="center">11</td>
    <td align="right">0.1134</td>
    <td align="right">32.16</td>
    <td align="right">56.05</td>
    <td align="right">39.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0181</td>
    <td align="right">49.18</td>
    <td align="right">97.89</td>
    <td align="right">97.69</td>
    <td align="center">14</td>
    <td align="right">0.0124</td>
    <td align="right">57.57</td>
    <td align="right">101.75</td>
    <td align="right">103.37</td>
    <td align="center">13</td>
    <td align="right">0.0253</td>
    <td align="right">32.18</td>
    <td align="right">57.25</td>
    <td align="right">40.81</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4533</td>
    <td align="right">23.05</td>
    <td align="right">27.57</td>
    <td align="right">27.80</td>
    <td align="center">5</td>
    <td align="right">2.4471</td>
    <td align="right">24.15</td>
    <td align="right">29.59</td>
    <td align="right">29.65</td>
    <td align="center">5</td>
    <td align="right">2.3272</td>
    <td align="right">24.53</td>
    <td align="right">30.63</td>
    <td align="right">30.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4375</td>
    <td align="right">23.65</td>
    <td align="right">47.59</td>
    <td align="right">35.63</td>
    <td align="center">8</td>
    <td align="right">0.4137</td>
    <td align="right">23.50</td>
    <td align="right">40.30</td>
    <td align="right">27.53</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">25.02</td>
    <td align="right">54.24</td>
    <td align="right">40.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0906</td>
    <td align="right">30.98</td>
    <td align="right">55.85</td>
    <td align="right">39.22</td>
    <td align="center">11</td>
    <td align="right">0.0740</td>
    <td align="right">34.78</td>
    <td align="right">62.77</td>
    <td align="right">44.57</td>
    <td align="center">11</td>
    <td align="right">0.0604</td>
    <td align="right">34.50</td>
    <td align="right">62.99</td>
    <td align="right">44.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">31.09</td>
    <td align="right">56.26</td>
    <td align="right">39.91</td>
    <td align="center">13</td>
    <td align="right">0.0145</td>
    <td align="right">35.12</td>
    <td align="right">65.13</td>
    <td align="right">45.01</td>
    <td align="center">14</td>
    <td align="right">0.0129</td>
    <td align="right">35.45</td>
    <td align="right">65.78</td>
    <td align="right">45.50</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">75.41</td>
    <td align="right">38.46</td>
    <td align="right">17.91</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">69.31</td>
    <td align="right">69.21</td>
    <td align="right">48.81</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">23.34</td>
    <td align="right">21.72</td>
    <td align="right">27.33</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">28.61</td>
    <td align="right">29.43</td>
    <td align="right">33.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">99.12</td>
    <td align="right">87.14</td>
    <td align="right">50.74</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">27.81</td>
    <td align="right">24.26</td>
    <td align="right">27.50</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">31.17</td>
    <td align="right">32.11</td>
    <td align="right">35.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">132.65</td>
    <td align="right">146.45</td>
    <td align="right">61.51</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">41.72</td>
    <td align="right">29.45</td>
    <td align="right">31.28</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">41.93</td>
    <td align="right">97.71</td>
    <td align="right">102.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">306.43</td>
    <td align="right">254.75</td>
    <td align="right">76.01</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">58.21</td>
    <td align="right">42.35</td>
    <td align="right">55.86</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">69.42</td>
    <td align="right">74.42</td>
    <td align="right">100.64</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">38.35</td>
    <td align="right">49.81</td>
    <td align="right">51.34</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">31.01</td>
    <td align="right">47.31</td>
    <td align="right">47.57</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">20.46</td>
    <td align="right">30.79</td>
    <td align="right">30.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">33.52</td>
    <td align="right">65.39</td>
    <td align="right">65.34</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">40.96</td>
    <td align="right">70.90</td>
    <td align="right">68.98</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">19.47</td>
    <td align="right">43.26</td>
    <td align="right">30.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">45.58</td>
    <td align="right">90.96</td>
    <td align="right">93.97</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">63.29</td>
    <td align="right">100.76</td>
    <td align="right">93.63</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">54.51</td>
    <td align="right">116.90</td>
    <td align="right">78.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">61.52</td>
    <td align="right">112.00</td>
    <td align="right">117.65</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">73.19</td>
    <td align="right">120.44</td>
    <td align="right">132.44</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">97.78</td>
    <td align="right">118.04</td>
    <td align="right">91.42</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4632</td>
    <td align="right">20.27</td>
    <td align="right">32.20</td>
    <td align="right">32.73</td>
    <td align="center">5</td>
    <td align="right">2.4414</td>
    <td align="right">22.29</td>
    <td align="right">34.76</td>
    <td align="right">35.76</td>
    <td align="center">5</td>
    <td align="right">2.3147</td>
    <td align="right">23.01</td>
    <td align="right">39.98</td>
    <td align="right">39.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4402</td>
    <td align="right">24.81</td>
    <td align="right">76.83</td>
    <td align="right">60.10</td>
    <td align="center">8</td>
    <td align="right">0.4194</td>
    <td align="right">22.50</td>
    <td align="right">50.68</td>
    <td align="right">33.12</td>
    <td align="center">8</td>
    <td align="right">0.3773</td>
    <td align="right">27.85</td>
    <td align="right">73.82</td>
    <td align="right">56.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0851</td>
    <td align="right">51.11</td>
    <td align="right">89.11</td>
    <td align="right">69.51</td>
    <td align="center">11</td>
    <td align="right">0.0779</td>
    <td align="right">39.53</td>
    <td align="right">69.99</td>
    <td align="right">44.70</td>
    <td align="center">11</td>
    <td align="right">0.0652</td>
    <td align="right">43.99</td>
    <td align="right">77.63</td>
    <td align="right">57.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">70.93</td>
    <td align="right">107.81</td>
    <td align="right">94.19</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">49.06</td>
    <td align="right">119.27</td>
    <td align="right">95.98</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">58.36</td>
    <td align="right">97.04</td>
    <td align="right">76.51</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1542</td>
    <td align="right">102.16</td>
    <td align="right">89.13</td>
    <td align="right">58.02</td>
    <td align="center">4</td>
    <td align="right">3.3491</td>
    <td align="right">32.05</td>
    <td align="right">28.04</td>
    <td align="right">32.49</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">34.80</td>
    <td align="right">33.97</td>
    <td align="right">37.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">167.41</td>
    <td align="right">145.25</td>
    <td align="right">61.89</td>
    <td align="center">5</td>
    <td align="right">1.0294</td>
    <td align="right">36.00</td>
    <td align="right">32.20</td>
    <td align="right">38.65</td>
    <td align="center">6</td>
    <td align="right">0.8254</td>
    <td align="right">40.87</td>
    <td align="right">49.98</td>
    <td align="right">66.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0451</td>
    <td align="right">346.30</td>
    <td align="right">197.43</td>
    <td align="right">88.07</td>
    <td align="center">6</td>
    <td align="right">0.4029</td>
    <td align="right">65.03</td>
    <td align="right">61.03</td>
    <td align="right">63.17</td>
    <td align="center">7</td>
    <td align="right">0.2903</td>
    <td align="right">95.17</td>
    <td align="right">52.49</td>
    <td align="right">49.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">483.62</td>
    <td align="right">386.71</td>
    <td align="right">87.71</td>
    <td align="center">7</td>
    <td align="right">0.1877</td>
    <td align="right">64.67</td>
    <td align="right">50.11</td>
    <td align="right">51.91</td>
    <td align="center">8</td>
    <td align="right">0.1191</td>
    <td align="right">77.79</td>
    <td align="right">74.42</td>
    <td align="right">74.23</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">32.57</td>
    <td align="right">49.60</td>
    <td align="right">51.30</td>
    <td align="center">5</td>
    <td align="right">2.3116</td>
    <td align="right">37.48</td>
    <td align="right">54.21</td>
    <td align="right">52.04</td>
    <td align="center">5</td>
    <td align="right">2.7250</td>
    <td align="right">26.15</td>
    <td align="right">31.72</td>
    <td align="right">32.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4206</td>
    <td align="right">39.02</td>
    <td align="right">74.48</td>
    <td align="right">77.50</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">54.65</td>
    <td align="right">116.74</td>
    <td align="right">138.17</td>
    <td align="center">8</td>
    <td align="right">0.5385</td>
    <td align="right">33.59</td>
    <td align="right">69.43</td>
    <td align="right">54.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0786</td>
    <td align="right">75.22</td>
    <td align="right">127.86</td>
    <td align="right">118.82</td>
    <td align="center">11</td>
    <td align="right">0.0636</td>
    <td align="right">106.04</td>
    <td align="right">137.02</td>
    <td align="right">133.71</td>
    <td align="center">11</td>
    <td align="right">0.1183</td>
    <td align="right">109.30</td>
    <td align="right">150.02</td>
    <td align="right">132.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">125.44</td>
    <td align="right">158.03</td>
    <td align="right">156.05</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">89.39</td>
    <td align="right">125.92</td>
    <td align="right">133.15</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">90.88</td>
    <td align="right">100.77</td>
    <td align="right">105.69</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4644</td>
    <td align="right">26.76</td>
    <td align="right">33.92</td>
    <td align="right">32.63</td>
    <td align="center">5</td>
    <td align="right">2.4405</td>
    <td align="right">26.36</td>
    <td align="right">33.19</td>
    <td align="right">33.15</td>
    <td align="center">5</td>
    <td align="right">2.3265</td>
    <td align="right">27.07</td>
    <td align="right">34.85</td>
    <td align="right">35.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4413</td>
    <td align="right">26.96</td>
    <td align="right">56.02</td>
    <td align="right">42.03</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">26.03</td>
    <td align="right">45.39</td>
    <td align="right">30.49</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">27.94</td>
    <td align="right">62.94</td>
    <td align="right">47.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0845</td>
    <td align="right">44.15</td>
    <td align="right">80.83</td>
    <td align="right">61.43</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">40.86</td>
    <td align="right">71.60</td>
    <td align="right">53.21</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">42.18</td>
    <td align="right">71.48</td>
    <td align="right">51.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">62.79</td>
    <td align="right">94.79</td>
    <td align="right">73.00</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">46.13</td>
    <td align="right">82.81</td>
    <td align="right">62.49</td>
    <td align="center">14</td>
    <td align="right">0.0116</td>
    <td align="right">44.79</td>
    <td align="right">84.94</td>
    <td align="right">61.34</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
